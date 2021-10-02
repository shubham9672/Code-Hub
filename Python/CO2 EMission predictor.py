{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "pd.plotting.register_matplotlib_converters()\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"CO2.xls\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Make', 'Model', 'Vehicle Class', 'Engine Size(L)', 'Cylinders',\n",
       "       'Transmission', 'Fuel Type', 'Fuel Consumption City (L/100 km)',\n",
       "       'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',\n",
       "       'Fuel Consumption Comb (mpg)', 'CO2 Emissions(g/km)'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Make                                 object\n",
       "Model                                object\n",
       "Vehicle Class                        object\n",
       "Engine Size(L)                      float64\n",
       "Cylinders                             int64\n",
       "Transmission                         object\n",
       "Fuel Type                            object\n",
       "Fuel Consumption City (L/100 km)    float64\n",
       "Fuel Consumption Hwy (L/100 km)     float64\n",
       "Fuel Consumption Comb (L/100 km)    float64\n",
       "Fuel Consumption Comb (mpg)           int64\n",
       "CO2 Emissions(g/km)                   int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Make</th>\n",
       "      <th>Model</th>\n",
       "      <th>Vehicle Class</th>\n",
       "      <th>Engine Size(L)</th>\n",
       "      <th>Cylinders</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Fuel Type</th>\n",
       "      <th>Fuel Consumption City (L/100 km)</th>\n",
       "      <th>Fuel Consumption Hwy (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (mpg)</th>\n",
       "      <th>CO2 Emissions(g/km)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS5</td>\n",
       "      <td>Z</td>\n",
       "      <td>9.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.5</td>\n",
       "      <td>33</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>M6</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.2</td>\n",
       "      <td>7.7</td>\n",
       "      <td>9.6</td>\n",
       "      <td>29</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX HYBRID</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>AV7</td>\n",
       "      <td>Z</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>5.9</td>\n",
       "      <td>48</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>MDX 4WD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.7</td>\n",
       "      <td>9.1</td>\n",
       "      <td>11.1</td>\n",
       "      <td>25</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>RDX AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.1</td>\n",
       "      <td>8.7</td>\n",
       "      <td>10.6</td>\n",
       "      <td>27</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Make       Model Vehicle Class  Engine Size(L)  Cylinders Transmission  \\\n",
       "0  ACURA         ILX       COMPACT             2.0          4          AS5   \n",
       "1  ACURA         ILX       COMPACT             2.4          4           M6   \n",
       "2  ACURA  ILX HYBRID       COMPACT             1.5          4          AV7   \n",
       "3  ACURA     MDX 4WD   SUV - SMALL             3.5          6          AS6   \n",
       "4  ACURA     RDX AWD   SUV - SMALL             3.5          6          AS6   \n",
       "\n",
       "  Fuel Type  Fuel Consumption City (L/100 km)  \\\n",
       "0         Z                               9.9   \n",
       "1         Z                              11.2   \n",
       "2         Z                               6.0   \n",
       "3         Z                              12.7   \n",
       "4         Z                              12.1   \n",
       "\n",
       "   Fuel Consumption Hwy (L/100 km)  Fuel Consumption Comb (L/100 km)  \\\n",
       "0                              6.7                               8.5   \n",
       "1                              7.7                               9.6   \n",
       "2                              5.8                               5.9   \n",
       "3                              9.1                              11.1   \n",
       "4                              8.7                              10.6   \n",
       "\n",
       "   Fuel Consumption Comb (mpg)  CO2 Emissions(g/km)  \n",
       "0                           33                  196  \n",
       "1                           29                  221  \n",
       "2                           48                  136  \n",
       "3                           25                  255  \n",
       "4                           27                  244  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Make                                  42\n",
       "Model                               2053\n",
       "Vehicle Class                         16\n",
       "Engine Size(L)                        51\n",
       "Cylinders                              8\n",
       "Transmission                          27\n",
       "Fuel Type                              5\n",
       "Fuel Consumption City (L/100 km)     211\n",
       "Fuel Consumption Hwy (L/100 km)      143\n",
       "Fuel Consumption Comb (L/100 km)     181\n",
       "Fuel Consumption Comb (mpg)           54\n",
       "CO2 Emissions(g/km)                  331\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(7385, 12)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Make                                0\n",
       "Model                               0\n",
       "Vehicle Class                       0\n",
       "Engine Size(L)                      0\n",
       "Cylinders                           0\n",
       "Transmission                        0\n",
       "Fuel Type                           0\n",
       "Fuel Consumption City (L/100 km)    0\n",
       "Fuel Consumption Hwy (L/100 km)     0\n",
       "Fuel Consumption Comb (L/100 km)    0\n",
       "Fuel Consumption Comb (mpg)         0\n",
       "CO2 Emissions(g/km)                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Make</th>\n",
       "      <th>Model</th>\n",
       "      <th>Vehicle Class</th>\n",
       "      <th>Engine Size(L)</th>\n",
       "      <th>Cylinders</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Fuel Type</th>\n",
       "      <th>Fuel Consumption City (L/100 km)</th>\n",
       "      <th>Fuel Consumption Hwy (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (mpg)</th>\n",
       "      <th>CO2 Emissions(g/km)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS5</td>\n",
       "      <td>Z</td>\n",
       "      <td>9.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.5</td>\n",
       "      <td>33</td>\n",
       "      <td>196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>M6</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.2</td>\n",
       "      <td>7.7</td>\n",
       "      <td>9.6</td>\n",
       "      <td>29</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>ILX HYBRID</td>\n",
       "      <td>COMPACT</td>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>AV7</td>\n",
       "      <td>Z</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>5.9</td>\n",
       "      <td>48</td>\n",
       "      <td>136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>MDX 4WD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.7</td>\n",
       "      <td>9.1</td>\n",
       "      <td>11.1</td>\n",
       "      <td>25</td>\n",
       "      <td>255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>ACURA</td>\n",
       "      <td>RDX AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>AS6</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.1</td>\n",
       "      <td>8.7</td>\n",
       "      <td>10.6</td>\n",
       "      <td>27</td>\n",
       "      <td>244</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7380</th>\n",
       "      <td>VOLVO</td>\n",
       "      <td>XC40 T5 AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS8</td>\n",
       "      <td>Z</td>\n",
       "      <td>10.7</td>\n",
       "      <td>7.7</td>\n",
       "      <td>9.4</td>\n",
       "      <td>30</td>\n",
       "      <td>219</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7381</th>\n",
       "      <td>VOLVO</td>\n",
       "      <td>XC60 T5 AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS8</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.2</td>\n",
       "      <td>8.3</td>\n",
       "      <td>9.9</td>\n",
       "      <td>29</td>\n",
       "      <td>232</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7382</th>\n",
       "      <td>VOLVO</td>\n",
       "      <td>XC60 T6 AWD</td>\n",
       "      <td>SUV - SMALL</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS8</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.7</td>\n",
       "      <td>8.6</td>\n",
       "      <td>10.3</td>\n",
       "      <td>27</td>\n",
       "      <td>240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7383</th>\n",
       "      <td>VOLVO</td>\n",
       "      <td>XC90 T5 AWD</td>\n",
       "      <td>SUV - STANDARD</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS8</td>\n",
       "      <td>Z</td>\n",
       "      <td>11.2</td>\n",
       "      <td>8.3</td>\n",
       "      <td>9.9</td>\n",
       "      <td>29</td>\n",
       "      <td>232</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7384</th>\n",
       "      <td>VOLVO</td>\n",
       "      <td>XC90 T6 AWD</td>\n",
       "      <td>SUV - STANDARD</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>AS8</td>\n",
       "      <td>Z</td>\n",
       "      <td>12.2</td>\n",
       "      <td>8.7</td>\n",
       "      <td>10.7</td>\n",
       "      <td>26</td>\n",
       "      <td>248</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>7385 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Make        Model   Vehicle Class  Engine Size(L)  Cylinders  \\\n",
       "0     ACURA          ILX         COMPACT             2.0          4   \n",
       "1     ACURA          ILX         COMPACT             2.4          4   \n",
       "2     ACURA   ILX HYBRID         COMPACT             1.5          4   \n",
       "3     ACURA      MDX 4WD     SUV - SMALL             3.5          6   \n",
       "4     ACURA      RDX AWD     SUV - SMALL             3.5          6   \n",
       "...     ...          ...             ...             ...        ...   \n",
       "7380  VOLVO  XC40 T5 AWD     SUV - SMALL             2.0          4   \n",
       "7381  VOLVO  XC60 T5 AWD     SUV - SMALL             2.0          4   \n",
       "7382  VOLVO  XC60 T6 AWD     SUV - SMALL             2.0          4   \n",
       "7383  VOLVO  XC90 T5 AWD  SUV - STANDARD             2.0          4   \n",
       "7384  VOLVO  XC90 T6 AWD  SUV - STANDARD             2.0          4   \n",
       "\n",
       "     Transmission Fuel Type  Fuel Consumption City (L/100 km)  \\\n",
       "0             AS5         Z                               9.9   \n",
       "1              M6         Z                              11.2   \n",
       "2             AV7         Z                               6.0   \n",
       "3             AS6         Z                              12.7   \n",
       "4             AS6         Z                              12.1   \n",
       "...           ...       ...                               ...   \n",
       "7380          AS8         Z                              10.7   \n",
       "7381          AS8         Z                              11.2   \n",
       "7382          AS8         Z                              11.7   \n",
       "7383          AS8         Z                              11.2   \n",
       "7384          AS8         Z                              12.2   \n",
       "\n",
       "      Fuel Consumption Hwy (L/100 km)  Fuel Consumption Comb (L/100 km)  \\\n",
       "0                                 6.7                               8.5   \n",
       "1                                 7.7                               9.6   \n",
       "2                                 5.8                               5.9   \n",
       "3                                 9.1                              11.1   \n",
       "4                                 8.7                              10.6   \n",
       "...                               ...                               ...   \n",
       "7380                              7.7                               9.4   \n",
       "7381                              8.3                               9.9   \n",
       "7382                              8.6                              10.3   \n",
       "7383                              8.3                               9.9   \n",
       "7384                              8.7                              10.7   \n",
       "\n",
       "      Fuel Consumption Comb (mpg)  CO2 Emissions(g/km)  \n",
       "0                              33                  196  \n",
       "1                              29                  221  \n",
       "2                              48                  136  \n",
       "3                              25                  255  \n",
       "4                              27                  244  \n",
       "...                           ...                  ...  \n",
       "7380                           30                  219  \n",
       "7381                           29                  232  \n",
       "7382                           27                  240  \n",
       "7383                           29                  232  \n",
       "7384                           26                  248  \n",
       "\n",
       "[7385 rows x 12 columns]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot:title={'center':'Engine Size(L)'}>,\n",
       "        <AxesSubplot:title={'center':'Cylinders'}>,\n",
       "        <AxesSubplot:title={'center':'Fuel Consumption City (L/100 km)'}>],\n",
       "       [<AxesSubplot:title={'center':'Fuel Consumption Hwy (L/100 km)'}>,\n",
       "        <AxesSubplot:title={'center':'Fuel Consumption Comb (L/100 km)'}>,\n",
       "        <AxesSubplot:title={'center':'Fuel Consumption Comb (mpg)'}>],\n",
       "       [<AxesSubplot:title={'center':'CO2 Emissions(g/km)'}>,\n",
       "        <AxesSubplot:>, <AxesSubplot:>]], dtype=object)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 9 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plt.figure(figsize=(16,6))\n",
    "sns.lineplot(data=df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'CO2 Emissions(g/km)')"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lineplot(data=df['Engine Size(L)'], label=\"Engine Size(L)\")\n",
    "sns.lineplot(data=df['Cylinders'], label=\"Cylinders\")\n",
    "plt.xlabel(\"CO2 Emissions(g/km)\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 0, 'Cylinders')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.lineplot(data=df['Fuel Consumption City (L/100 km)'], label=\"Fuel Consumption City (L/100 km)\")\n",
    "sns.lineplot(data=df['Fuel Consumption Hwy (L/100 km)'], label=\"Fuel Consumption Hwy (L/100 km\")\n",
    "plt.xlabel(\"Cylinders\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Cylinders', ylabel='CO2 Emissions(g/km)'>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x=df[\"Cylinders\"], y=df[\"CO2 Emissions(g/km)\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4     3220\n",
       "6     2446\n",
       "8     1402\n",
       "12     151\n",
       "3       95\n",
       "10      42\n",
       "5       26\n",
       "16       3\n",
       "Name: Cylinders, dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Cylinders\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Fuel Type', ylabel='CO2 Emissions(g/km)'>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x=df[\"Fuel Type\"], y=df[\"CO2 Emissions(g/km)\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "label=df[\"CO2 Emissions(g/km)\"]\n",
    "df=df.drop([\"Model\",\"CO2 Emissions(g/km)\"],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Make', 'Vehicle Class', 'Engine Size(L)', 'Cylinders', 'Transmission',\n",
       "       'Fuel Type', 'Fuel Consumption City (L/100 km)',\n",
       "       'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)',\n",
       "       'Fuel Consumption Comb (mpg)'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.drop(['Make','Vehicle Class','Transmission','Fuel Type'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=df\n",
    "y=label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Engine Size(L)</th>\n",
       "      <th>Cylinders</th>\n",
       "      <th>Fuel Consumption City (L/100 km)</th>\n",
       "      <th>Fuel Consumption Hwy (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (L/100 km)</th>\n",
       "      <th>Fuel Consumption Comb (mpg)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.0</td>\n",
       "      <td>4</td>\n",
       "      <td>9.9</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.5</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.4</td>\n",
       "      <td>4</td>\n",
       "      <td>11.2</td>\n",
       "      <td>7.7</td>\n",
       "      <td>9.6</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.5</td>\n",
       "      <td>4</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.8</td>\n",
       "      <td>5.9</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>12.7</td>\n",
       "      <td>9.1</td>\n",
       "      <td>11.1</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>6</td>\n",
       "      <td>12.1</td>\n",
       "      <td>8.7</td>\n",
       "      <td>10.6</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Engine Size(L)  Cylinders  Fuel Consumption City (L/100 km)  \\\n",
       "0             2.0          4                               9.9   \n",
       "1             2.4          4                              11.2   \n",
       "2             1.5          4                               6.0   \n",
       "3             3.5          6                              12.7   \n",
       "4             3.5          6                              12.1   \n",
       "\n",
       "   Fuel Consumption Hwy (L/100 km)  Fuel Consumption Comb (L/100 km)  \\\n",
       "0                              6.7                               8.5   \n",
       "1                              7.7                               9.6   \n",
       "2                              5.8                               5.9   \n",
       "3                              9.1                              11.1   \n",
       "4                              8.7                              10.6   \n",
       "\n",
       "   Fuel Consumption Comb (mpg)  \n",
       "0                           33  \n",
       "1                           29  \n",
       "2                           48  \n",
       "3                           25  \n",
       "4                           27  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    196\n",
       "1    221\n",
       "2    136\n",
       "3    255\n",
       "4    244\n",
       "Name: CO2 Emissions(g/km), dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split \n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, \n",
    "                                                    random_state=0) \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error, r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regression_model = LinearRegression()\n",
    "regression_model.fit(X_train, y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4.70383385,  7.76959907, -1.51477993,  2.73761068,  4.8658569 ,\n",
       "       -3.38982683])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regression_model.coef_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "226.0599025226596"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regression_model.intercept_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predicted = regression_model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[249.65304846 203.45885259 261.64474078 ... 241.13691986 171.40953612\n",
      " 257.40502822]\n"
     ]
    }
   ],
   "source": [
    "print(y_predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train Score:  0.9070615085206077\n",
      "Test Score:  0.8973258718836304\n"
     ]
    }
   ],
   "source": [
    "    print('Train Score: ',regression_model .score(X_train, y_train))  \n",
    "    print('Test Score: ', regression_model.score(X_test, y_test))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6307    241\n",
      "5036    229\n",
      "1995    253\n",
      "4156    183\n",
      "6328    231\n",
      "       ... \n",
      "4627    325\n",
      "5336    300\n",
      "4425    232\n",
      "6725    170\n",
      "491     246\n",
      "Name: CO2 Emissions(g/km), Length: 2438, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean absolute error: 11.55\n",
      "Residual sum of squares (MSE): 349.93\n",
      "R2-score: 0.89\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import r2_score\n",
    "\n",
    "\n",
    "print(\"Mean absolute error: %.2f\" % np.mean(np.absolute(y_predicted - y_test)))\n",
    "print(\"Residual sum of squares (MSE): %.2f\" % np.mean((y_predicted - y_test) ** 2))\n",
    "print(\"R2-score: %.2f\" % r2_score(y_predicted , y_test) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "ename": "EOFError",
     "evalue": "Ran out of input",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mEOFError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-34-ef74d8525700>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# dump information to that file\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mregression_model\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfile\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mmodel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'co2_final.pkl'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'rb'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mEOFError\u001b[0m: Ran out of input"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "# open a file, where you ant to store the data\n",
    "file = open('co2_final.pkl', 'wb')\n",
    "\n",
    "# dump information to that file\n",
    "pickle.dump(regression_model, file)\n",
    "model = pickle.load(open('co2_final.pkl','rb'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
