/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.getsales.helper;

/**
 *
 * @author student
 */
public class Sales {
    private int updateID;
    private String storeID;
    private String date;
    private String salesAmount;
    private String costAmount;
    private String profit;

    public Sales(String storeID, String date, String salesAmount, String costAmount, String profit) {
        this.storeID = storeID;
        this.date = date;
        this.salesAmount = salesAmount;
        this.costAmount = costAmount;
        this.profit = profit;
    }

    public int getUpdateID() {
        return updateID;
    }

    public void setUpdateID(int updateID) {
        this.updateID = updateID;
    }

    public String getStoreID() {
        return storeID;
    }

    public void setStoreID(String storeID) {
        this.storeID = storeID;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getSalesAmount() {
        return salesAmount;
    }

    public void setSalesAmount(String salesAmount) {
        this.salesAmount = salesAmount;
    }

    public String getCostAmount() {
        return costAmount;
    }

    public void setCostAmount(String costAmount) {
        this.costAmount = costAmount;
    }

    public String getProfit() {
        return profit;
    }

    public void setProfit(String profit) {
        this.profit = profit;
    }

    @Override
    public String toString() {
        return "Sales{" +
                "updateID=" + updateID +
                ", storeID=" + storeID +
                ", date='" + date + '\'' +
                ", salesAmount='" + salesAmount + '\'' +
                ", costAmount='" + costAmount + '\'' +
                ", profit='" + profit + '\'' +
                '}';
    }
}
