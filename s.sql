SELECT oi.OrderID,
       SUM(oi.Quantity * s.Quantity * m.Price) AS Total
FROM OrderItems oi
JOIN Specifications s ON oi.ProductID = s.ProductID
JOIN Materials m ON s.MaterialID = m.MaterialID
GROUP BY oi.OrderID;