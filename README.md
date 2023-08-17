定期投資計算工具
這是一個工具，可以計算在固定的投資金額與固定的月利率下，經過特定月數後的總投資回報。

功能
自動從 setting.xml 中讀取投資參數。
計算固定投資與月利率下的最終回報。
輸出結果至 result.txt 檔案。
使用方式
確保您已有 setting.xml 設定檔。
在 setting.xml 中設定以下參數：
money: 一個月要投資的金額（例如：1000）。
interest: 每個月的利息率（例如：10 表示 10%）。
month: 要投資的月份（例如：1 表示 1 個月）。
xml
Copy code
<data>
    <money>1000</money>
    <interest>10</interest>
    <month>1</month>
</data>
執行已轉換為 exe 的程式。
程式將根據設定的參數計算最終的投資回報，並將結果保存到 result.txt 檔案中。
您可以打開 result.txt 查看計算結果。
注意事項
確保 setting.xml 的格式正確，且所有的值都是整數。
如果修改了 setting.xml 設定，需重新執行程式來獲取新的計算結果。
這只是一個基本的 readme.md，您可以根據需要進行調整和擴展。希望這對您有所幫助！
