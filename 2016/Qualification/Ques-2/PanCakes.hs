import Data.List (groupBy)
getCount xs | length xs == 1 = if ((head xs) !! 0 == '+') then 0 else 1
            | last xs !! 0 == '-' = length xs
            | head xs !! 0 == '-' = length xs -1
            | otherwise = length xs
              
getInstanceCount = getCount . groupBy (==)
