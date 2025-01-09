package ryerson.ca.getsales.business;

import io.grpc.stub.StreamObserver;
import io.kubemq.sdk.basic.ServerAddressNotSuppliedException;
import io.kubemq.sdk.event.EventReceive;
import io.kubemq.sdk.event.Subscriber;
import io.kubemq.sdk.subscription.EventsStoreType;
import io.kubemq.sdk.subscription.SubscribeRequest;
import io.kubemq.sdk.subscription.SubscribeType;
import io.kubemq.sdk.tools.Converter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.net.ssl.SSLException;
import ryerson.ca.getsales.persistence.Finance_CRUD;
import ryerson.ca.getsales.helper.Sales;

public class Messaging {
    public static void Receiving_Events_Store(String cname) throws SSLException, ServerAddressNotSuppliedException {
        String ChannelName = cname, ClientID = "hello-world-subscriber";
        String kubeMQAddress = System.getenv("kubeMQAddress");
        Subscriber subscriber = new Subscriber(kubeMQAddress);
        SubscribeRequest subscribeRequest = new SubscribeRequest();
        subscribeRequest.setChannel(ChannelName);
        subscribeRequest.setClientID(ClientID);
        subscribeRequest.setSubscribeType(SubscribeType.EventsStore);
        subscribeRequest.setEventsStoreType(EventsStoreType.StartAtSequence);
        subscribeRequest.setEventsStoreTypeValue(1);

        StreamObserver<EventReceive> streamObserver = new StreamObserver<EventReceive>() {
            @Override
            public void onNext(EventReceive value) {
                try {
                    String message = (String) Converter.FromByteArray(value.getBody());
                    System.out.printf("Event Received: EventID: %s, Channel: %s, Metadata: %s, Body: %s\n",
                            value.getEventId(), value.getChannel(), value.getMetadata(), message);
                    String[] msgParts = message.split(":");
                    if (msgParts.length >= 6) { // Check if message has at least 6 parts
                        String storeID = msgParts[1];
                        String date = msgParts[2];
                        String salesAmount = msgParts[3];
                        String costAmount = msgParts[4];
                        String profit = msgParts[5];
                        Finance_CRUD financeCrud = new Finance_CRUD();
                        Sales sale = new Sales(storeID, date, salesAmount, costAmount, profit);
                        boolean done;
                        done = financeCrud.addSales(sale);
                    } else {
                        System.out.println("Invalid message format: " + message);
                    }
                } catch (ClassNotFoundException e) {
                    System.out.printf("ClassNotFoundException: %s\n", e.getMessage());
                    e.printStackTrace();
                } catch (IOException e) {
                    System.out.printf("IOException: %s\n", e.getMessage());
                    e.printStackTrace();
                } catch (ArrayIndexOutOfBoundsException e) {
                    System.out.printf("ArrayIndexOutOfBoundsException: %s\n", e.getMessage());
                    e.printStackTrace();
                }
            }

            @Override
            public void onError(Throwable t) {
                System.out.printf("onError:  %s\n", t.getMessage());
            }

            @Override
            public void onCompleted() {

            }
        };
        subscriber.SubscribeToEvents(subscribeRequest, streamObserver);
    }
}


