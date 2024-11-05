{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Content Based Recommender System On E-Commerce Data**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Importing Packages and Loading the data**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import ast\n",
    "import plotly.express as px\n",
    "from plotly import graph_objects as go"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('flipkart_com-ecommerce_sample.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>uniq_id</th>\n",
       "      <th>crawl_timestamp</th>\n",
       "      <th>product_url</th>\n",
       "      <th>product_name</th>\n",
       "      <th>product_category_tree</th>\n",
       "      <th>pid</th>\n",
       "      <th>retail_price</th>\n",
       "      <th>discounted_price</th>\n",
       "      <th>image</th>\n",
       "      <th>is_FK_Advantage_product</th>\n",
       "      <th>description</th>\n",
       "      <th>product_rating</th>\n",
       "      <th>overall_rating</th>\n",
       "      <th>brand</th>\n",
       "      <th>product_specifications</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>c2d766ca982eca8304150849735ffef9</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/alisha-solid-women-s-c...</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[\"Clothing &gt;&gt; Women's Clothing &gt;&gt; Lingerie, Sl...</td>\n",
       "      <td>SRTEH2FF9KEDEFGF</td>\n",
       "      <td>999.0</td>\n",
       "      <td>379.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/short/u/4/a/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Alisha</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7f7036a6d550aaa89d34c77bd39a5e48</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/fabhomedecor-fabric-do...</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed</td>\n",
       "      <td>[\"Furniture &gt;&gt; Living Room Furniture &gt;&gt; Sofa B...</td>\n",
       "      <td>SBEEH3QGU7MFYJFY</td>\n",
       "      <td>32157.0</td>\n",
       "      <td>22646.0</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/sofa-bed/j/f...</td>\n",
       "      <td>False</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed (Finish Co...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>FabHomeDecor</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Installati...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>f449ec65dcbc041b6ae5e6a32717d01b</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/aw-bellies/p/itmeh4grg...</td>\n",
       "      <td>AW Bellies</td>\n",
       "      <td>[\"Footwear &gt;&gt; Women's Footwear &gt;&gt; Ballerinas &gt;...</td>\n",
       "      <td>SHOEH4GRSUBJGZXE</td>\n",
       "      <td>999.0</td>\n",
       "      <td>499.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/shoe/7/z/z/r...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of AW Bellies Sandals Wedges Heel...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>AW</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Ideal For\"...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0973b37acd0c664e3de26e97e5571454</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/alisha-solid-women-s-c...</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[\"Clothing &gt;&gt; Women's Clothing &gt;&gt; Lingerie, Sl...</td>\n",
       "      <td>SRTEH2F6HUZMQ6SJ</td>\n",
       "      <td>699.0</td>\n",
       "      <td>267.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/short/6/2/h/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Alisha</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>bc940ea42ee6bef5ac7cea3fb5cfbee7</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/sicons-all-purpose-arn...</td>\n",
       "      <td>Sicons All Purpose Arnica Dog Shampoo</td>\n",
       "      <td>[\"Pet Supplies &gt;&gt; Grooming &gt;&gt; Skin &amp; Coat Care...</td>\n",
       "      <td>PSOEH3ZYDMSYARJ5</td>\n",
       "      <td>220.0</td>\n",
       "      <td>210.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/pet-shampoo/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Specifications of Sicons All Purpose Arnica Do...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Sicons</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Pet Type\",...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            uniq_id            crawl_timestamp  \\\n",
       "0  c2d766ca982eca8304150849735ffef9  2016-03-25 22:59:23 +0000   \n",
       "1  7f7036a6d550aaa89d34c77bd39a5e48  2016-03-25 22:59:23 +0000   \n",
       "2  f449ec65dcbc041b6ae5e6a32717d01b  2016-03-25 22:59:23 +0000   \n",
       "3  0973b37acd0c664e3de26e97e5571454  2016-03-25 22:59:23 +0000   \n",
       "4  bc940ea42ee6bef5ac7cea3fb5cfbee7  2016-03-25 22:59:23 +0000   \n",
       "\n",
       "                                         product_url  \\\n",
       "0  http://www.flipkart.com/alisha-solid-women-s-c...   \n",
       "1  http://www.flipkart.com/fabhomedecor-fabric-do...   \n",
       "2  http://www.flipkart.com/aw-bellies/p/itmeh4grg...   \n",
       "3  http://www.flipkart.com/alisha-solid-women-s-c...   \n",
       "4  http://www.flipkart.com/sicons-all-purpose-arn...   \n",
       "\n",
       "                            product_name  \\\n",
       "0    Alisha Solid Women's Cycling Shorts   \n",
       "1    FabHomeDecor Fabric Double Sofa Bed   \n",
       "2                             AW Bellies   \n",
       "3    Alisha Solid Women's Cycling Shorts   \n",
       "4  Sicons All Purpose Arnica Dog Shampoo   \n",
       "\n",
       "                               product_category_tree               pid  \\\n",
       "0  [\"Clothing >> Women's Clothing >> Lingerie, Sl...  SRTEH2FF9KEDEFGF   \n",
       "1  [\"Furniture >> Living Room Furniture >> Sofa B...  SBEEH3QGU7MFYJFY   \n",
       "2  [\"Footwear >> Women's Footwear >> Ballerinas >...  SHOEH4GRSUBJGZXE   \n",
       "3  [\"Clothing >> Women's Clothing >> Lingerie, Sl...  SRTEH2F6HUZMQ6SJ   \n",
       "4  [\"Pet Supplies >> Grooming >> Skin & Coat Care...  PSOEH3ZYDMSYARJ5   \n",
       "\n",
       "   retail_price  discounted_price  \\\n",
       "0         999.0             379.0   \n",
       "1       32157.0           22646.0   \n",
       "2         999.0             499.0   \n",
       "3         699.0             267.0   \n",
       "4         220.0             210.0   \n",
       "\n",
       "                                               image  is_FK_Advantage_product  \\\n",
       "0  [\"http://img5a.flixcart.com/image/short/u/4/a/...                    False   \n",
       "1  [\"http://img6a.flixcart.com/image/sofa-bed/j/f...                    False   \n",
       "2  [\"http://img5a.flixcart.com/image/shoe/7/z/z/r...                    False   \n",
       "3  [\"http://img5a.flixcart.com/image/short/6/2/h/...                    False   \n",
       "4  [\"http://img5a.flixcart.com/image/pet-shampoo/...                    False   \n",
       "\n",
       "                                         description       product_rating  \\\n",
       "0  Key Features of Alisha Solid Women's Cycling S...  No rating available   \n",
       "1  FabHomeDecor Fabric Double Sofa Bed (Finish Co...  No rating available   \n",
       "2  Key Features of AW Bellies Sandals Wedges Heel...  No rating available   \n",
       "3  Key Features of Alisha Solid Women's Cycling S...  No rating available   \n",
       "4  Specifications of Sicons All Purpose Arnica Do...  No rating available   \n",
       "\n",
       "        overall_rating         brand  \\\n",
       "0  No rating available        Alisha   \n",
       "1  No rating available  FabHomeDecor   \n",
       "2  No rating available            AW   \n",
       "3  No rating available        Alisha   \n",
       "4  No rating available        Sicons   \n",
       "\n",
       "                              product_specifications  \n",
       "0  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "1  {\"product_specification\"=>[{\"key\"=>\"Installati...  \n",
       "2  {\"product_specification\"=>[{\"key\"=>\"Ideal For\"...  \n",
       "3  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "4  {\"product_specification\"=>[{\"key\"=>\"Pet Type\",...  "
      ]
     },
     "execution_count": 3,
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
   "execution_count": 4,
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
       "      <th>uniq_id</th>\n",
       "      <th>crawl_timestamp</th>\n",
       "      <th>product_url</th>\n",
       "      <th>product_name</th>\n",
       "      <th>product_category_tree</th>\n",
       "      <th>pid</th>\n",
       "      <th>retail_price</th>\n",
       "      <th>discounted_price</th>\n",
       "      <th>image</th>\n",
       "      <th>is_FK_Advantage_product</th>\n",
       "      <th>description</th>\n",
       "      <th>product_rating</th>\n",
       "      <th>overall_rating</th>\n",
       "      <th>brand</th>\n",
       "      <th>product_specifications</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>19995</th>\n",
       "      <td>7179d2f6c4ad50a17d014ca1d2815156</td>\n",
       "      <td>2015-12-01 10:15:43 +0000</td>\n",
       "      <td>http://www.flipkart.com/walldesign-small-vinyl...</td>\n",
       "      <td>WallDesign Small Vinyl Sticker</td>\n",
       "      <td>[\"Baby Care &gt;&gt; Baby &amp; Kids Gifts &gt;&gt; Stickers &gt;...</td>\n",
       "      <td>STIE7KFJAKSTDY9G</td>\n",
       "      <td>1500.0</td>\n",
       "      <td>730.0</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/wall-decorat...</td>\n",
       "      <td>False</td>\n",
       "      <td>Buy WallDesign Small Vinyl Sticker for Rs.730 ...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>WallDesign</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19996</th>\n",
       "      <td>71ac419198359d37b8fe5e3fffdfee09</td>\n",
       "      <td>2015-12-01 10:15:43 +0000</td>\n",
       "      <td>http://www.flipkart.com/wallmantra-large-vinyl...</td>\n",
       "      <td>Wallmantra Large Vinyl Stickers Sticker</td>\n",
       "      <td>[\"Baby Care &gt;&gt; Baby &amp; Kids Gifts &gt;&gt; Stickers &gt;...</td>\n",
       "      <td>STIE9F5URNQGJCGH</td>\n",
       "      <td>1429.0</td>\n",
       "      <td>1143.0</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/sticker/z/g/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Buy Wallmantra Large Vinyl Stickers Sticker fo...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Wallmantra</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19997</th>\n",
       "      <td>93e9d343837400ce0d7980874ece471c</td>\n",
       "      <td>2015-12-01 10:15:43 +0000</td>\n",
       "      <td>http://www.flipkart.com/elite-collection-mediu...</td>\n",
       "      <td>Elite Collection Medium Acrylic Sticker</td>\n",
       "      <td>[\"Baby Care &gt;&gt; Baby &amp; Kids Gifts &gt;&gt; Stickers &gt;...</td>\n",
       "      <td>STIE7VAYDKQZEBSD</td>\n",
       "      <td>1299.0</td>\n",
       "      <td>999.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/sticker/b/s/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Buy Elite Collection Medium Acrylic Sticker fo...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Elite Collection</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19998</th>\n",
       "      <td>669e79b8fa5d9ae020841c0c97d5e935</td>\n",
       "      <td>2015-12-01 10:15:43 +0000</td>\n",
       "      <td>http://www.flipkart.com/elite-collection-mediu...</td>\n",
       "      <td>Elite Collection Medium Acrylic Sticker</td>\n",
       "      <td>[\"Baby Care &gt;&gt; Baby &amp; Kids Gifts &gt;&gt; Stickers &gt;...</td>\n",
       "      <td>STIE8YSVEPPCZ42Y</td>\n",
       "      <td>1499.0</td>\n",
       "      <td>1199.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/sticker/4/2/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Buy Elite Collection Medium Acrylic Sticker fo...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Elite Collection</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19999</th>\n",
       "      <td>cb4fa87a874f715fff567f7b7b3be79c</td>\n",
       "      <td>2015-12-01 10:15:43 +0000</td>\n",
       "      <td>http://www.flipkart.com/elite-collection-mediu...</td>\n",
       "      <td>Elite Collection Medium Acrylic Sticker</td>\n",
       "      <td>[\"Baby Care &gt;&gt; Baby &amp; Kids Gifts &gt;&gt; Stickers &gt;...</td>\n",
       "      <td>STIE88KN9ZDSGZKY</td>\n",
       "      <td>1499.0</td>\n",
       "      <td>999.0</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/sticker/z/k/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Buy Elite Collection Medium Acrylic Sticker fo...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Elite Collection</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                uniq_id            crawl_timestamp  \\\n",
       "19995  7179d2f6c4ad50a17d014ca1d2815156  2015-12-01 10:15:43 +0000   \n",
       "19996  71ac419198359d37b8fe5e3fffdfee09  2015-12-01 10:15:43 +0000   \n",
       "19997  93e9d343837400ce0d7980874ece471c  2015-12-01 10:15:43 +0000   \n",
       "19998  669e79b8fa5d9ae020841c0c97d5e935  2015-12-01 10:15:43 +0000   \n",
       "19999  cb4fa87a874f715fff567f7b7b3be79c  2015-12-01 10:15:43 +0000   \n",
       "\n",
       "                                             product_url  \\\n",
       "19995  http://www.flipkart.com/walldesign-small-vinyl...   \n",
       "19996  http://www.flipkart.com/wallmantra-large-vinyl...   \n",
       "19997  http://www.flipkart.com/elite-collection-mediu...   \n",
       "19998  http://www.flipkart.com/elite-collection-mediu...   \n",
       "19999  http://www.flipkart.com/elite-collection-mediu...   \n",
       "\n",
       "                                  product_name  \\\n",
       "19995           WallDesign Small Vinyl Sticker   \n",
       "19996  Wallmantra Large Vinyl Stickers Sticker   \n",
       "19997  Elite Collection Medium Acrylic Sticker   \n",
       "19998  Elite Collection Medium Acrylic Sticker   \n",
       "19999  Elite Collection Medium Acrylic Sticker   \n",
       "\n",
       "                                   product_category_tree               pid  \\\n",
       "19995  [\"Baby Care >> Baby & Kids Gifts >> Stickers >...  STIE7KFJAKSTDY9G   \n",
       "19996  [\"Baby Care >> Baby & Kids Gifts >> Stickers >...  STIE9F5URNQGJCGH   \n",
       "19997  [\"Baby Care >> Baby & Kids Gifts >> Stickers >...  STIE7VAYDKQZEBSD   \n",
       "19998  [\"Baby Care >> Baby & Kids Gifts >> Stickers >...  STIE8YSVEPPCZ42Y   \n",
       "19999  [\"Baby Care >> Baby & Kids Gifts >> Stickers >...  STIE88KN9ZDSGZKY   \n",
       "\n",
       "       retail_price  discounted_price  \\\n",
       "19995        1500.0             730.0   \n",
       "19996        1429.0            1143.0   \n",
       "19997        1299.0             999.0   \n",
       "19998        1499.0            1199.0   \n",
       "19999        1499.0             999.0   \n",
       "\n",
       "                                                   image  \\\n",
       "19995  [\"http://img6a.flixcart.com/image/wall-decorat...   \n",
       "19996  [\"http://img6a.flixcart.com/image/sticker/z/g/...   \n",
       "19997  [\"http://img5a.flixcart.com/image/sticker/b/s/...   \n",
       "19998  [\"http://img5a.flixcart.com/image/sticker/4/2/...   \n",
       "19999  [\"http://img6a.flixcart.com/image/sticker/z/k/...   \n",
       "\n",
       "       is_FK_Advantage_product  \\\n",
       "19995                    False   \n",
       "19996                    False   \n",
       "19997                    False   \n",
       "19998                    False   \n",
       "19999                    False   \n",
       "\n",
       "                                             description       product_rating  \\\n",
       "19995  Buy WallDesign Small Vinyl Sticker for Rs.730 ...  No rating available   \n",
       "19996  Buy Wallmantra Large Vinyl Stickers Sticker fo...  No rating available   \n",
       "19997  Buy Elite Collection Medium Acrylic Sticker fo...  No rating available   \n",
       "19998  Buy Elite Collection Medium Acrylic Sticker fo...  No rating available   \n",
       "19999  Buy Elite Collection Medium Acrylic Sticker fo...  No rating available   \n",
       "\n",
       "            overall_rating             brand  \\\n",
       "19995  No rating available        WallDesign   \n",
       "19996  No rating available        Wallmantra   \n",
       "19997  No rating available  Elite Collection   \n",
       "19998  No rating available  Elite Collection   \n",
       "19999  No rating available  Elite Collection   \n",
       "\n",
       "                                  product_specifications  \n",
       "19995  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "19996  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "19997  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "19998  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "19999  {\"product_specification\"=>[{\"key\"=>\"Number of ...  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Exploratory Data Analysis**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20000, 15)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's print the shape of the dataset\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20000 entries, 0 to 19999\n",
      "Data columns (total 15 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   uniq_id                  20000 non-null  object \n",
      " 1   crawl_timestamp          20000 non-null  object \n",
      " 2   product_url              20000 non-null  object \n",
      " 3   product_name             20000 non-null  object \n",
      " 4   product_category_tree    20000 non-null  object \n",
      " 5   pid                      20000 non-null  object \n",
      " 6   retail_price             19922 non-null  float64\n",
      " 7   discounted_price         19922 non-null  float64\n",
      " 8   image                    19997 non-null  object \n",
      " 9   is_FK_Advantage_product  20000 non-null  bool   \n",
      " 10  description              19998 non-null  object \n",
      " 11  product_rating           20000 non-null  object \n",
      " 12  overall_rating           20000 non-null  object \n",
      " 13  brand                    14136 non-null  object \n",
      " 14  product_specifications   19986 non-null  object \n",
      "dtypes: bool(1), float64(2), object(12)\n",
      "memory usage: 2.2+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
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
       "Index(['uniq_id', 'crawl_timestamp', 'product_url', 'product_name',\n",
       "       'product_category_tree', 'pid', 'retail_price', 'discounted_price',\n",
       "       'image', 'is_FK_Advantage_product', 'description', 'product_rating',\n",
       "       'overall_rating', 'brand', 'product_specifications'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's print the column names in the data\n",
    "df.columns"
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
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "19995    False\n",
       "19996    False\n",
       "19997    False\n",
       "19998    False\n",
       "19999    False\n",
       "Length: 20000, dtype: bool"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's check the duplicated values in our dataset\n",
    "df.duplicated()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's check the total duplicated values in our dataset\n",
    "df.duplicated().sum()"
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
       "uniq_id                       0\n",
       "crawl_timestamp               0\n",
       "product_url                   0\n",
       "product_name                  0\n",
       "product_category_tree         0\n",
       "pid                           0\n",
       "retail_price                 78\n",
       "discounted_price             78\n",
       "image                         3\n",
       "is_FK_Advantage_product       0\n",
       "description                   2\n",
       "product_rating                0\n",
       "overall_rating                0\n",
       "brand                      5864\n",
       "product_specifications       14\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
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
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TheLostPuppy Back Cover for Apple iPad Air               134\n",
       "TheLostPuppy Back Cover for Apple iPad Air 2              95\n",
       "S4S Stylish Women's Push-up Bra                           94\n",
       "Voylla Metal, Alloy Necklace                              66\n",
       "WallDesign Small Vinyl Sticker                            65\n",
       "                                                        ... \n",
       "Floret Comfortable Women's T-Shirt Bra                     1\n",
       "Ladyland Life White Women's Full Coverage Bra              1\n",
       "BM WOOD FURNITURE Hexagon Wall Shelves MDF Wall Shelf      1\n",
       "Amora Women Wedges                                         1\n",
       "Imitzworld Alloy Choker                                    1\n",
       "Name: product_name, Length: 12676, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's check the total number of unique products in our data \n",
    "df.product_name.value_counts()"
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
       "uniq_id                    20000\n",
       "crawl_timestamp              371\n",
       "product_url                20000\n",
       "product_name               12676\n",
       "product_category_tree       6466\n",
       "pid                        19998\n",
       "retail_price                2247\n",
       "discounted_price            2448\n",
       "image                      18589\n",
       "is_FK_Advantage_product        2\n",
       "description                17539\n",
       "product_rating                36\n",
       "overall_rating                36\n",
       "brand                       3499\n",
       "product_specifications     18825\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's check the unique values in our data\n",
    "df.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
       "      <th>count</th>\n",
       "      <th>unique</th>\n",
       "      <th>top</th>\n",
       "      <th>freq</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>uniq_id</th>\n",
       "      <td>20000</td>\n",
       "      <td>20000</td>\n",
       "      <td>7b5635a04b19ce17c7b9470ca0e18a5b</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>crawl_timestamp</th>\n",
       "      <td>20000</td>\n",
       "      <td>371</td>\n",
       "      <td>2015-12-01 12:40:44 +0000</td>\n",
       "      <td>1979</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_url</th>\n",
       "      <td>20000</td>\n",
       "      <td>20000</td>\n",
       "      <td>http://www.flipkart.com/vaishna-fashion-women-...</td>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_name</th>\n",
       "      <td>20000</td>\n",
       "      <td>12676</td>\n",
       "      <td>TheLostPuppy Back Cover for Apple iPad Air</td>\n",
       "      <td>134</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_category_tree</th>\n",
       "      <td>20000</td>\n",
       "      <td>6466</td>\n",
       "      <td>[\"Jewellery &gt;&gt; Necklaces &amp; Chains &gt;&gt; Necklaces\"]</td>\n",
       "      <td>1567</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pid</th>\n",
       "      <td>20000</td>\n",
       "      <td>19998</td>\n",
       "      <td>ACCEJ6TESY7AFT5W</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>retail_price</th>\n",
       "      <td>19922</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2979.21</td>\n",
       "      <td>9009.64</td>\n",
       "      <td>35</td>\n",
       "      <td>666</td>\n",
       "      <td>1040</td>\n",
       "      <td>1999</td>\n",
       "      <td>571230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>discounted_price</th>\n",
       "      <td>19922</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1973.4</td>\n",
       "      <td>7333.59</td>\n",
       "      <td>35</td>\n",
       "      <td>350</td>\n",
       "      <td>550</td>\n",
       "      <td>999</td>\n",
       "      <td>571230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>image</th>\n",
       "      <td>19997</td>\n",
       "      <td>18589</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/car-mat/m/t/...</td>\n",
       "      <td>45</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>is_FK_Advantage_product</th>\n",
       "      <td>20000</td>\n",
       "      <td>2</td>\n",
       "      <td>False</td>\n",
       "      <td>19215</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <td>19998</td>\n",
       "      <td>17539</td>\n",
       "      <td>TheLostPuppy Back Cover for Apple iPad Air (Mu...</td>\n",
       "      <td>92</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_rating</th>\n",
       "      <td>20000</td>\n",
       "      <td>36</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>18151</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>overall_rating</th>\n",
       "      <td>20000</td>\n",
       "      <td>36</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>18151</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>brand</th>\n",
       "      <td>14136</td>\n",
       "      <td>3499</td>\n",
       "      <td>Allure Auto</td>\n",
       "      <td>469</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>product_specifications</th>\n",
       "      <td>19986</td>\n",
       "      <td>18825</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Type\", \"va...</td>\n",
       "      <td>71</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         count unique  \\\n",
       "uniq_id                  20000  20000   \n",
       "crawl_timestamp          20000    371   \n",
       "product_url              20000  20000   \n",
       "product_name             20000  12676   \n",
       "product_category_tree    20000   6466   \n",
       "pid                      20000  19998   \n",
       "retail_price             19922    NaN   \n",
       "discounted_price         19922    NaN   \n",
       "image                    19997  18589   \n",
       "is_FK_Advantage_product  20000      2   \n",
       "description              19998  17539   \n",
       "product_rating           20000     36   \n",
       "overall_rating           20000     36   \n",
       "brand                    14136   3499   \n",
       "product_specifications   19986  18825   \n",
       "\n",
       "                                                                       top  \\\n",
       "uniq_id                                   7b5635a04b19ce17c7b9470ca0e18a5b   \n",
       "crawl_timestamp                                  2015-12-01 12:40:44 +0000   \n",
       "product_url              http://www.flipkart.com/vaishna-fashion-women-...   \n",
       "product_name                    TheLostPuppy Back Cover for Apple iPad Air   \n",
       "product_category_tree     [\"Jewellery >> Necklaces & Chains >> Necklaces\"]   \n",
       "pid                                                       ACCEJ6TESY7AFT5W   \n",
       "retail_price                                                           NaN   \n",
       "discounted_price                                                       NaN   \n",
       "image                    [\"http://img6a.flixcart.com/image/car-mat/m/t/...   \n",
       "is_FK_Advantage_product                                              False   \n",
       "description              TheLostPuppy Back Cover for Apple iPad Air (Mu...   \n",
       "product_rating                                         No rating available   \n",
       "overall_rating                                         No rating available   \n",
       "brand                                                          Allure Auto   \n",
       "product_specifications   {\"product_specification\"=>[{\"key\"=>\"Type\", \"va...   \n",
       "\n",
       "                          freq     mean      std  min  25%   50%   75%     max  \n",
       "uniq_id                      1      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "crawl_timestamp           1979      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "product_url                  1      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "product_name               134      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "product_category_tree     1567      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "pid                          2      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "retail_price               NaN  2979.21  9009.64   35  666  1040  1999  571230  \n",
       "discounted_price           NaN   1973.4  7333.59   35  350   550   999  571230  \n",
       "image                       45      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "is_FK_Advantage_product  19215      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "description                 92      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "product_rating           18151      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "overall_rating           18151      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "brand                      469      NaN      NaN  NaN  NaN   NaN   NaN     NaN  \n",
       "product_specifications      71      NaN      NaN  NaN  NaN   NaN   NaN     NaN  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Let's check the statistical analysis of the data\n",
    "df.describe(include='all').T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"retail_price\"].fillna(df[\"retail_price\"].median(),inplace=True)\n",
    "df[\"discounted_price\"].fillna(df[\"discounted_price\"].median(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df['retail_price']-df['discounted_price']\n",
    "y=(x/df['retail_price'])*100\n",
    "df['discount_percentage']=y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['timestamp']=pd.to_datetime(df['crawl_timestamp'])  \n",
    "df['Time']=df['timestamp'].apply(lambda x : x.time)  \n",
    "df['date']=df['timestamp'].apply(lambda x : x.date)  \n",
    "df.drop(['crawl_timestamp'], axis = 1,inplace=True)  \n",
    "df['main_category']=df['product_category_tree'].apply(lambda x :x.split('>>')[0][2:len(x.split('>>')[0])-1])  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 10\n",
    "top_products=pd.DataFrame(df['main_category'].value_counts()  [:n]).reset_index()\n",
    "top_products.rename(columns = {'index':'Top_Products','main_category':'Total_Count'}, inplace = True)\n",
    "\n",
    "#Top 10 main brands being purchased\n",
    "\n",
    "n = 10\n",
    "top_brands=pd.DataFrame(df['brand'].value_counts()[:n]).reset_index()\n",
    "top_brands.rename(columns = {'index':'Top_Brands','brand':'Total_Count'}, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "domain": {
          "x": [
           0,
           0.45
          ],
          "y": [
           0,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "label+percent+name",
         "labels": [
          "Clothing",
          "Jewellery",
          "Footwear",
          "Mobiles & Accessories",
          "Automotive",
          "Home Decor & Festive Needs",
          "Beauty and Personal Care",
          "Home Furnishing",
          "Kitchen & Dining",
          "Computers"
         ],
         "name": "Top Products",
         "pull": [
          0.3,
          0,
          0,
          0
         ],
         "type": "pie",
         "values": [
          6198,
          3531,
          1227,
          1099,
          1012,
          929,
          710,
          700,
          647,
          578
         ]
        },
        {
         "domain": {
          "x": [
           0.55,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "label+percent+name",
         "labels": [
          "Allure Auto",
          "Regular",
          "Voylla",
          "Slim",
          "TheLostPuppy",
          "Karatcraft",
          "Black",
          "White",
          "DailyObjects",
          "Speedwav"
         ],
         "name": "Top Brands",
         "pull": [
          0.3,
          0,
          0,
          0
         ],
         "type": "pie",
         "values": [
          469,
          313,
          299,
          288,
          229,
          211,
          167,
          155,
          144,
          141
         ]
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {
           "size": 20
          },
          "showarrow": false,
          "text": "Product",
          "x": 0.18,
          "y": 0.5
         },
         {
          "font": {
           "size": 20
          },
          "showarrow": false,
          "text": "Brand",
          "x": 0.82,
          "y": 0.5
         }
        ],
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Top products and brands distribution"
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from plotly.subplots import make_subplots\n",
    "\n",
    "label1 = top_products['Top_Products']\n",
    "value1=top_products['Total_Count']\n",
    "label2=top_brands['Top_Brands']\n",
    "value2=top_brands['Total_Count']\n",
    "\n",
    "# Create subplots\n",
    "\n",
    "fig_both = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])\n",
    "fig_both.add_trace(go.Pie(labels=label1, values=value1, name=\"Top Products\",pull=[0.3, 0, 0, 0]),\n",
    "              1, 1)\n",
    "fig_both.add_trace(go.Pie(labels=label2, values=value2, name=\"Top Brands\",pull=[0.3, 0, 0, 0]),\n",
    "              1, 2)\n",
    "\n",
    "# Use `hole` to create a donut-like pie chart\n",
    "\n",
    "fig_both.update_traces(hole=.4, hoverinfo=\"label+percent+name\")\n",
    "#fig_both.update_traces(hoverinfo=\"label+percent+name\")\n",
    "\n",
    "fig_both.update_layout(\n",
    "    title_text=\"Top products and brands distribution\",\n",
    "    #Add annotations in the center of the donut pies\n",
    "    \n",
    "    annotations=[dict(text='Product', x=0.18, y=0.5, font_size=20, showarrow=False),\n",
    "                 dict(text='Brand', x=0.82, y=0.5, font_size=20, showarrow=False)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_discount=df.query('discount_percentage > 90')  #targeting brands giving high discounts\n",
    "df_discount=df_discount.dropna() #dropping rows with NA values\n",
    "df_discount[\"brand\"].replace('FashBlush','Fash Blush',inplace=True) #handling spelling errors\n",
    "max_discount=pd.DataFrame(df_discount.groupby('brand')[['discount_percentage']].mean().sort_values(by=['discount_percentage'],ascending=False).reset_index())  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Rajcrafts",
         "marker": {
          "color": "rgb(27,158,119)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Rajcrafts",
         "offsetgroup": "Rajcrafts",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Rajcrafts"
         ],
         "xaxis": "x",
         "y": [
          96.53333333333333
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Bling",
         "marker": {
          "color": "rgb(217,95,2)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Bling",
         "offsetgroup": "Bling",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Bling"
         ],
         "xaxis": "x",
         "y": [
          94.54845814977973
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Fash Blush",
         "marker": {
          "color": "rgb(117,112,179)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Fash Blush",
         "offsetgroup": "Fash Blush",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Fash Blush"
         ],
         "xaxis": "x",
         "y": [
          92.71171363460957
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Mydress Mystyle",
         "marker": {
          "color": "rgb(231,41,138)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Mydress Mystyle",
         "offsetgroup": "Mydress Mystyle",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Mydress Mystyle"
         ],
         "xaxis": "x",
         "y": [
          91.991991991992
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Soulful Threads",
         "marker": {
          "color": "rgb(102,166,30)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Soulful Threads",
         "offsetgroup": "Soulful Threads",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Soulful Threads"
         ],
         "xaxis": "x",
         "y": [
          91.9526627218935
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Instella",
         "marker": {
          "color": "rgb(230,171,2)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Instella",
         "offsetgroup": "Instella",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Instella"
         ],
         "xaxis": "x",
         "y": [
          91.71974522292994
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Bond Beatz",
         "marker": {
          "color": "rgb(166,118,29)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Bond Beatz",
         "offsetgroup": "Bond Beatz",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Bond Beatz"
         ],
         "xaxis": "x",
         "y": [
          91.59663865546219
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Fashblush",
         "marker": {
          "color": "rgb(102,102,102)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Fashblush",
         "offsetgroup": "Fashblush",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Fashblush"
         ],
         "xaxis": "x",
         "y": [
          91.13252498311718
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Black",
         "marker": {
          "color": "rgb(27,158,119)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Black",
         "offsetgroup": "Black",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Black"
         ],
         "xaxis": "x",
         "y": [
          90.6816760475297
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "KazamaKraft",
         "marker": {
          "color": "rgb(217,95,2)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "KazamaKraft",
         "offsetgroup": "KazamaKraft",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "KazamaKraft"
         ],
         "xaxis": "x",
         "y": [
          90.56561840204466
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Zaicus",
         "marker": {
          "color": "rgb(117,112,179)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Zaicus",
         "offsetgroup": "Zaicus",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Zaicus"
         ],
         "xaxis": "x",
         "y": [
          90.14328063241108
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "CUBA",
         "marker": {
          "color": "rgb(231,41,138)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "CUBA",
         "offsetgroup": "CUBA",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "CUBA"
         ],
         "xaxis": "x",
         "y": [
          90.04502251125562
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "SDZ",
         "marker": {
          "color": "rgb(102,166,30)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "SDZ",
         "offsetgroup": "SDZ",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "SDZ"
         ],
         "xaxis": "x",
         "y": [
          90.04502251125562
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hovertemplate": "brand=%{x}<br>discount_percentage=%{y}<extra></extra>",
         "legendgroup": "Gia",
         "marker": {
          "color": "rgb(230,171,2)",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Gia",
         "offsetgroup": "Gia",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Gia"
         ],
         "xaxis": "x",
         "y": [
          90.02000444543232
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "title": {
          "text": "brand"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "categoryarray": [
          "Rajcrafts",
          "Bling",
          "Fash Blush",
          "Mydress Mystyle",
          "Soulful Threads",
          "Instella",
          "Bond Beatz",
          "Fashblush",
          "Black",
          "KazamaKraft",
          "Zaicus",
          "CUBA",
          "SDZ",
          "Gia"
         ],
         "categoryorder": "array",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "brand"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "discount_percentage"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "px.bar(max_discount, x= 'brand', y='discount_percentage',color='brand',color_discrete_sequence=px.colors.qualitative.Dark2)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "uniq_id=%{x}<br>discounted_price=%{marker.color}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": [
           571230,
           201000,
           162825,
           141375,
           132990,
           116292,
           107750,
           105300,
           86500,
           70785,
           70785,
           70200,
           68400,
           65900,
           61800,
           60840,
           57500,
           55575,
           54795,
           53300
          ],
          "coloraxis": "coloraxis",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "329c5f4d7aced63e1ce3e88f41d5e7e6",
          "08452abdadb3db1e686b94a9c52fc7b6",
          "3a2546675bc399953779e58d84d56650",
          "d9fa5b1d8917b841abaef2a1ce032114",
          "07b0df742cdcac28d09c29a1e246fff2",
          "c4b045288524a8770c760ed2bbca2ed5",
          "710ed5f2393a4b9e8823aa0029f71f93",
          "dd96000fa1d9e408a4fc47ea5c1123e5",
          "eb15c8c168e9ebb8d24deac65e0aec37",
          "30f324f95b6f5c26284893d0d85becf1",
          "5f8e0c25e2915bc2383e60ad02b1e4aa",
          "e794bd226967af2298a2c7a1f8e2c9bb",
          "e3e08f67f1e0b5724e71c6845a7f0ffa",
          "b92dedcdcec57fe018148b9b2db237f7",
          "069a49081494492829bd914203a8bd52",
          "44ac0b6808242ce5c71b971d7620c609",
          "43e444307157aca6bb055c4bada67928",
          "1b1c83326a749b99c9cafc740f9136fa",
          "e0de6958769d030f7e470e590f374d24",
          "f923846a4f6ed68abe553a11d1d938d2"
         ],
         "xaxis": "x",
         "y": [
          571230,
          201000,
          162825,
          141375,
          132990,
          116292,
          107750,
          105300,
          86500,
          70785,
          70785,
          70200,
          68400,
          65900,
          61800,
          60840,
          57500,
          55575,
          54795,
          53300
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "discounted_price"
          }
         },
         "colorscale": [
          [
           0,
           "rgb(84,48,5)"
          ],
          [
           0.1,
           "rgb(140,81,10)"
          ],
          [
           0.2,
           "rgb(191,129,45)"
          ],
          [
           0.3,
           "rgb(223,194,125)"
          ],
          [
           0.4,
           "rgb(246,232,195)"
          ],
          [
           0.5,
           "rgb(245,245,245)"
          ],
          [
           0.6,
           "rgb(199,234,229)"
          ],
          [
           0.7,
           "rgb(128,205,193)"
          ],
          [
           0.8,
           "rgb(53,151,143)"
          ],
          [
           0.9,
           "rgb(1,102,94)"
          ],
          [
           1,
           "rgb(0,60,48)"
          ]
         ]
        },
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "uniq_id"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "discounted_price"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_customer=df.groupby(\"uniq_id\")[[\"discounted_price\"]].sum().sort_values(by=['discounted_price'],ascending=[False]).reset_index()\n",
    "\n",
    "#Top 20 customers spending the most\n",
    "list1=df_customer[:20]\n",
    "\n",
    "#plotting a bar graph\n",
    "px.bar(list1, x= 'uniq_id', y=\"discounted_price\",color='discounted_price',color_continuous_scale=px.colors.diverging.BrBG)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "number=%{x}<br>stage=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa"
         },
         "name": "",
         "orientation": "h",
         "showlegend": false,
         "type": "funnel",
         "x": [
          20000,
          1849,
          620
         ],
         "xaxis": "x",
         "y": [
          "Total Products",
          "Products with ratings",
          "Products with 5 star rating"
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "number"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "stage"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 5 star rating\n",
    "\n",
    "total_prod=len(df['pid'])  #total products using pid variable\n",
    "total_ratings=len(df[df['product_rating']!='No rating available']) #total rated products\n",
    "top_ratings=len(df[df['product_rating']=='5']) #5 star rated products\n",
    "df_funnel_1 = dict(\n",
    "    number=[total_prod,total_ratings,top_ratings],\n",
    "    stage=[\"Total Products\",\"Products with ratings\",\"Products with 5 star rating\"])\n",
    "funnel_1_fig = px.funnel(df_funnel_1, x='number', y='stage')\n",
    "funnel_1_fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#5 star products/brands\n",
    "rating_5=pd.DataFrame(df.loc[df['product_rating'] == '5'])\n",
    "top_product_type=rating_5['main_category'].value_counts() #top products\n",
    "top_brand_type=rating_5['brand'].value_counts()  #top brands\n",
    "\n",
    "#top 5 products\n",
    "df_top_product=pd.DataFrame(top_product_type[:5].reset_index()) #first 5\n",
    "df_top_product.rename(columns = {'index':'top_prod'}, inplace = True) \n",
    "df_top_product.drop('main_category', inplace=True, axis=1)\n",
    "\n",
    "#top 5 brands\n",
    "df_top_brand=pd.DataFrame(top_brand_type[:5].reset_index())\n",
    "df_top_brand.rename(columns = {'index':'top_brands'}, inplace = True)\n",
    "df_top_brand.drop('brand', inplace=True, axis=1)\n",
    "df_top_brand.head()\n",
    "\n",
    "#concatenating the 2 tables\n",
    "df_product_brand_rate5=pd.concat([df_top_product,df_top_brand],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "marker": {
          "color": "crimson",
          "size": 12
         },
         "mode": "markers",
         "name": "ratings",
         "type": "scatter",
         "x": [
          5,
          4,
          1,
          3,
          2,
          4.5,
          3.7,
          4.2,
          4.3,
          3.5,
          3.6,
          4.7,
          4.1,
          3.8,
          2.5,
          4.8,
          3.2,
          3.3,
          4.4,
          3.9,
          3.4,
          2.3,
          2.8,
          2.7,
          4.6,
          2.2,
          3.1,
          2.9,
          2.4,
          1.3,
          4.9,
          1.7,
          1.5,
          2.6,
          1.8
         ],
         "y": [
          620,
          246,
          171,
          168,
          80,
          67,
          51,
          47,
          45,
          45,
          25,
          24,
          24,
          23,
          23,
          21,
          20,
          17,
          16,
          15,
          13,
          12,
          11,
          10,
          9,
          8,
          7,
          5,
          5,
          4,
          4,
          4,
          4,
          3,
          2
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Ratings v/s Count"
        },
        "xaxis": {
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "title": {
          "text": "Ratings"
         }
        },
        "yaxis": {
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "title": {
          "text": "Count"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.drop(df.index[df['product_rating'] == 'No rating available'], inplace = True) \n",
    "ratings=pd.DataFrame(df['product_rating'].value_counts().reset_index())\n",
    "ratings['index'] = ratings['index'].astype(float)\n",
    "ratings.head().sort_values(by=['index'],ascending=[False])\n",
    "ratings.rename(columns = {'index':'Ratings','product_rating':'Counts'}, inplace = True)\n",
    "\n",
    "#plotting the result\n",
    "data=ratings\n",
    "x=ratings['Ratings']\n",
    "y=ratings['Counts']\n",
    "figdot2 = go.Figure()\n",
    "figdot2.add_trace(go.Scatter(\n",
    "    x=x,\n",
    "    y=y,\n",
    "    marker=dict(color=\"crimson\", size=12),\n",
    "    mode=\"markers\",\n",
    "    name=\"ratings\",\n",
    "))\n",
    "\n",
    "figdot2.update_layout(title=\"Ratings v/s Count\",\n",
    "                  xaxis_title=\"Ratings\",\n",
    "                  yaxis_title=\"Count\",\n",
    "                     )\n",
    "\n",
    "figdot2.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "figdot2.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "figdot2.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "fill": "tozeroy",
         "line": {
          "color": "crimson",
          "width": 0.5
         },
         "name": "retail price",
         "type": "scatter",
         "x": [
          "2015-12-01",
          "2015-12-03",
          "2015-12-04",
          "2015-12-06",
          "2015-12-12",
          "2015-12-13",
          "2015-12-15",
          "2015-12-20",
          "2015-12-29",
          "2015-12-30",
          "2015-12-31",
          "2016-01-01",
          "2016-01-02",
          "2016-01-03",
          "2016-01-04",
          "2016-01-06",
          "2016-01-07",
          "2016-02-24",
          "2016-02-25",
          "2016-02-28",
          "2016-03-02",
          "2016-03-03",
          "2016-03-06",
          "2016-03-07",
          "2016-03-11",
          "2016-03-12",
          "2016-03-18",
          "2016-03-19",
          "2016-03-23",
          "2016-03-25",
          "2016-03-28",
          "2016-04-01",
          "2016-04-02",
          "2016-04-05",
          "2016-04-11",
          "2016-04-13",
          "2016-04-18",
          "2016-04-19",
          "2016-04-20",
          "2016-04-21",
          "2016-04-23",
          "2016-04-24",
          "2016-04-25",
          "2016-04-29",
          "2016-05-01",
          "2016-05-02",
          "2016-05-03",
          "2016-05-05",
          "2016-05-06",
          "2016-05-10",
          "2016-05-12",
          "2016-05-16",
          "2016-05-20",
          "2016-05-21",
          "2016-05-26",
          "2016-06-04",
          "2016-06-07",
          "2016-06-09",
          "2016-06-17",
          "2016-06-21",
          "2016-06-24",
          "2016-06-26"
         ],
         "y": [
          2220.5588235294117,
          1184.1,
          1963.8055555555557,
          1474.3076923076924,
          1340.3023255813953,
          836.6470588235294,
          777.6,
          1169.5744680851064,
          1652.3333333333333,
          1071.304347826087,
          4181.651515151515,
          3147.144578313253,
          1537,
          1963.5,
          1614.6153846153845,
          1460.3333333333333,
          1237.2038369304557,
          1714.3333333333333,
          6911,
          2356.8571428571427,
          900,
          1190.875,
          3099,
          424.5,
          1199,
          1599,
          2222,
          599,
          999,
          2787.6666666666665,
          1199,
          549,
          711.5625,
          1399,
          2864.3333333333335,
          1047.5,
          749,
          1900,
          998,
          699,
          1399,
          2199,
          6250,
          498.5,
          3499,
          3195,
          3999,
          700,
          288,
          618.6923076923077,
          499,
          999,
          5999,
          799,
          1949,
          499,
          1666,
          1999,
          1185.3333333333333,
          1199,
          1424,
          1150
         ]
        },
        {
         "fill": "tozeroy",
         "line": {
          "color": "darkslategray",
          "width": 0.5
         },
         "name": "discount price",
         "type": "scatter",
         "x": [
          "2015-12-01",
          "2015-12-03",
          "2015-12-04",
          "2015-12-06",
          "2015-12-12",
          "2015-12-13",
          "2015-12-15",
          "2015-12-20",
          "2015-12-29",
          "2015-12-30",
          "2015-12-31",
          "2016-01-01",
          "2016-01-02",
          "2016-01-03",
          "2016-01-04",
          "2016-01-06",
          "2016-01-07",
          "2016-02-24",
          "2016-02-25",
          "2016-02-28",
          "2016-03-02",
          "2016-03-03",
          "2016-03-06",
          "2016-03-07",
          "2016-03-11",
          "2016-03-12",
          "2016-03-18",
          "2016-03-19",
          "2016-03-23",
          "2016-03-25",
          "2016-03-28",
          "2016-04-01",
          "2016-04-02",
          "2016-04-05",
          "2016-04-11",
          "2016-04-13",
          "2016-04-18",
          "2016-04-19",
          "2016-04-20",
          "2016-04-21",
          "2016-04-23",
          "2016-04-24",
          "2016-04-25",
          "2016-04-29",
          "2016-05-01",
          "2016-05-02",
          "2016-05-03",
          "2016-05-05",
          "2016-05-06",
          "2016-05-10",
          "2016-05-12",
          "2016-05-16",
          "2016-05-20",
          "2016-05-21",
          "2016-05-26",
          "2016-06-04",
          "2016-06-07",
          "2016-06-09",
          "2016-06-17",
          "2016-06-21",
          "2016-06-24",
          "2016-06-26"
         ],
         "y": [
          1408.8991596638655,
          826.9,
          1045.3055555555557,
          606.8461538461538,
          735.5658914728682,
          569.6911764705883,
          563.6,
          697.2127659574468,
          1157.69918699187,
          417.9619565217391,
          2490.212121212121,
          2271.734939759036,
          937,
          1386.3333333333333,
          978.7692307692307,
          880.3333333333334,
          904.3549160671463,
          1232.3333333333333,
          4060.75,
          1995.7142857142858,
          399,
          514,
          2049,
          284.5,
          449,
          749,
          949.5,
          440,
          519,
          1553,
          247,
          299,
          450.1875,
          699,
          2516,
          556.5,
          297,
          874,
          598,
          699,
          758.6666666666666,
          1199,
          3480,
          249,
          1450,
          699,
          2999,
          399,
          288,
          395.1923076923077,
          449,
          249,
          1399,
          399,
          889,
          449,
          716,
          999,
          485.3333333333333,
          249,
          764,
          569
         ]
        }
       ],
       "layout": {
        "plot_bgcolor": "white",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "title": {
          "text": "Dates"
         }
        },
        "yaxis": {
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "title": {
          "text": "Price (in 1000s)"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df_date_retail = pd.DataFrame(df.groupby(\"date\")[[\"retail_price\"]].mean().reset_index())\n",
    "df_date_discount = pd.DataFrame(df.groupby(\"date\")[[\"discounted_price\"]].mean().reset_index())\n",
    "df_date_price=pd.concat([df_date_retail,df_date_discount],axis=1)\n",
    "df_date_price = df_date_price.loc[:,~df_date_price.columns.duplicated()] #remove duplicate columns\n",
    "\n",
    "#Plot\n",
    "x=df_date_price['date']\n",
    "y1=df_date_price['retail_price']\n",
    "y2=df_date_price['discounted_price']\n",
    "\n",
    "fig_area2 = go.Figure()\n",
    "fig_area2.add_trace(go.Scatter(x=x, y=y1, fill='tozeroy',name='retail price',\n",
    "                               line=dict(width=0.5, color='crimson'))) # fill down to xaxis\n",
    "fig_area2.add_trace(go.Scatter(x=x, y=y2, fill='tozeroy',name='discount price',\n",
    "                               line=dict(width=0.5, color='darkslategray')\n",
    "                              )) # fill to trace0 y\n",
    "\n",
    "fig_area2.update_layout(\n",
    "    xaxis_title=\"Dates\",\n",
    "    yaxis_title=\"Price (in 1000s)\",\n",
    "    plot_bgcolor='white'\n",
    ")\n",
    "fig_area2.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "fig_area2.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "fig_area2.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "x=%{x}<br>y=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "",
         "showlegend": false,
         "type": "scattergl",
         "x": [
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:17:46",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:20:04",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:29:55",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "00:54:41",
          "02:02:09",
          "02:13:26",
          "02:13:26",
          "02:17:20",
          "02:17:20",
          "02:17:20",
          "02:22:28",
          "02:22:28",
          "02:35:32",
          "02:50:54",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:01:47",
          "03:14:16",
          "03:25:23",
          "03:32:26",
          "03:32:26",
          "03:32:26",
          "03:49:23",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:32:43",
          "04:33:06",
          "04:50:59",
          "04:50:59",
          "05:00:32",
          "05:00:32",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:07:38",
          "05:11:30",
          "05:33:34",
          "05:33:34",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "05:50:25",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:04:02",
          "06:06:42",
          "06:06:42",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:13:00",
          "06:19:54",
          "06:19:54",
          "06:19:54",
          "06:19:54",
          "06:19:54",
          "07:04:11",
          "07:09:32",
          "07:09:32",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:25:36",
          "07:38:18",
          "07:42:43",
          "07:48:11",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:26:17",
          "08:40:28",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:19:31",
          "09:39:44",
          "09:39:44",
          "09:39:44",
          "09:45:55",
          "09:50:31",
          "09:50:31",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:15:43",
          "10:31:02",
          "10:31:02",
          "10:35:37",
          "10:36:58",
          "10:36:58",
          "10:36:58",
          "10:36:58",
          "10:36:58",
          "10:36:58",
          "10:36:58",
          "10:55:30",
          "10:55:30",
          "10:55:30",
          "10:55:30",
          "11:21:33",
          "11:26:55",
          "11:26:55",
          "11:45:32",
          "11:45:32",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:46:53",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "11:57:25",
          "12:13:08",
          "12:20:35",
          "12:20:35",
          "12:20:35",
          "12:20:35",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "12:40:44",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:15:34",
          "13:31:11",
          "13:48:35",
          "13:48:35",
          "14:06:00",
          "14:06:00",
          "14:06:00",
          "14:13:36",
          "14:13:36",
          "14:13:36",
          "14:18:51",
          "14:23:13",
          "14:25:06",
          "14:27:08",
          "14:30:46",
          "14:36:32",
          "15:23:58",
          "15:28:37",
          "15:45:50",
          "16:02:05",
          "16:02:05",
          "16:03:26",
          "16:03:26",
          "16:23:11",
          "16:30:14",
          "16:43:01",
          "17:07:54",
          "17:27:56",
          "17:56:58",
          "17:57:30",
          "18:16:52",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:20:45",
          "18:34:50",
          "18:34:50",
          "19:09:22",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:26:28",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:37:22",
          "19:42:22",
          "19:45:35",
          "20:03:13",
          "20:34:29",
          "20:56:50",
          "21:22:15",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "21:49:05",
          "22:49:41",
          "22:49:41",
          "22:59:23",
          "23:09:59",
          "23:09:59",
          "23:09:59",
          "23:09:59"
         ],
         "xaxis": "x",
         "y": [
          "http://www.flipkart.com/ladela-bellies/p/itmeh4kmxght7tuc?pid=SHOEH4KM2W3Z6EH5",
          "http://www.flipkart.com/bulaky-vanity-case-jewellery/p/itmdzy4ycfjhvctj?pid=VANDZY4YZFPEG85T",
          "http://www.flipkart.com/roadster-men-s-zipper-solid-cardigan/p/itmedfy7ueuk5mfs?pid=CGNEDFY77SGZTEQ2",
          "http://www.flipkart.com/camerii-wm64-elegance-analog-watch-men-boys/p/itme6y6duhfcummh?pid=WATE6Y6D2MZHWGBZ",
          "http://www.flipkart.com/colat-colat-mw20-sheen-analog-watch-men-women-boys-girls/p/itme2rx9jpyxcyqc?pid=WATE2RX9HHGBUQGA",
          "http://www.flipkart.com/rorlig-rr-028-expedition-analog-watch-men-boys/p/itmebyzgghrmgbnf?pid=WATEBYZGFCZPUJAR",
          "http://www.flipkart.com/lyc-white-casual-boots/p/itme96sz8vzhacqv?pid=SHOE4UC3MJZF3VFJ",
          "http://www.flipkart.com/fluid-dmf-002-gr01-digital-watch-boys/p/itme4cgcdzuhejcx?pid=WATE4CG2AQAGWGSF",
          "http://www.flipkart.com/bruno-manetti-cannelita-boots/p/itmeygk5jzcbzeh7?pid=SHOEYGK5AYYBVXKH",
          "http://www.flipkart.com/kool-kidz-dmk-012-qu02-analog-watch-girls-boys/p/itmdzdgtdarvvxtp?pid=WATDZDGRQBXTKHPW",
          "http://www.flipkart.com/kool-kidz-dmk-003-yl-03-analog-watch-girls-boys/p/itmduk7dkxv8wcaw?pid=WATDUK7DKXV8WCAW",
          "http://www.flipkart.com/kielz-ladies-boots/p/itmef9g7dygfgdet?pid=SHOEF9G8CVWHRH5M",
          "http://www.flipkart.com/colat-colat-m08-roman-numerals-analog-watch-men-boys/p/itme2rx9gtfueffm?pid=WATE2RX9CHBGEDRC",
          "http://www.flipkart.com/kielz-ladies-boots/p/itmefmrzgbtukpzc?pid=SHOEFMRZZAXFQW4F",
          "http://www.flipkart.com/srushti-art-jewelry-megnet-led-sport-blackred1-digital-watch-men-women-boys-girls/p/itmedfhaphf34yy8?pid=WATEDFHARG4YSPCA",
          "http://www.flipkart.com/q-q-vq13-008-analog-watch-girls-boys/p/itmduhdbdttvemws?pid=WATDUHDBDTTVEMWS",
          "http://www.flipkart.com/jack-klein-blackled-digital-watch-boys/p/itmeayzj7fcpxgpy?pid=WATEAYZJBFJXB4FZ",
          "http://www.flipkart.com/north-moon-iw-005-fk-silicone-ion-digital-watch-boys-girls-women/p/itme6gaqdmuyr2tz?pid=WATE6GAQSZYB3FKY",
          "http://www.flipkart.com/roadster-skinny-fit-men-s-jeans/p/itme8czgkzup3wgf?pid=JEAE8CZGJ8PGGHRQ",
          "http://www.flipkart.com/q-q-lla2-213-digital-watch-boys-girls/p/itmdz9cehwyqvfrt?pid=WATDZ9CEZAQHHTZ6",
          "http://www.flipkart.com/belle-gambe-winter-boots/p/itmefzxrgg9mgwxc?pid=SHOEFZXRNYJKPPYG",
          "http://www.flipkart.com/hala-red-black-trendy-digital-watch-boys-girls-men/p/itmeauab79jvz5jd?pid=WATEAUABHVPGRBAS",
          "http://www.flipkart.com/carlton-london-boots/p/itmdzzzyg9rnpven?pid=SHOECB92BGNGSZGZ",
          "http://www.flipkart.com/ridas-apl-led-black-apple-shape-digital-watch-boys/p/itme695ydcsmjrfn?pid=WATE695YXNTDWTE8",
          "http://www.flipkart.com/la-briza-andria-boots/p/itmey8mdgz8a5j2h?pid=SHOEFAJ5TYC2JMCH",
          "http://www.flipkart.com/skmei-1070blk-sports-analog-digital-watch-men-boys/p/itme8b5kfyzqabtj?pid=WATE8B5KWSTMZK7P",
          "http://www.flipkart.com/felix-3541-w-s-metal-analog-watch-boys-girls/p/itmeb5ezx3vuqyym?pid=WATEB5EZRN3NYXAG",
          "http://www.flipkart.com/steppings-trendy-boots/p/itme96vefbs3gatf?pid=SHOE2FQCR89ZNN8W",
          "http://www.flipkart.com/jack-klein-goldjack-analog-watch-boys-men/p/itme9cfhtm9zgmgt?pid=WATE9CFHPAEU3G4B",
          "http://www.flipkart.com/dearfoams-boots/p/itme8na5rhwecqtp?pid=SHOE8NA5SUXGYGYY",
          "http://www.flipkart.com/alfajr-wq18-qibla-compass-digital-watch-men-boys-girls/p/itmecgg4ybbwegzf?pid=WATECGG4W76YEBUB",
          "http://www.flipkart.com/3wish-cur-blue-silver-blue-8023-analog-watch-boys-men/p/itmece85hud3z3mj?pid=WATECE855W5YFE3H",
          "http://www.flipkart.com/belle-gambe-boots/p/itmec9fzjrfkfynk?pid=SHOEC9FZ7W9HTAQG",
          "http://www.flipkart.com/elantra-s-10-analog-watch-boys-men/p/itmec87guzuc8vzt?pid=WATEC87GMAMZAMWA",
          "http://www.flipkart.com/marvel-dw100243-digital-watch-boys-girls/p/itme3gezjyzdheff?pid=WATE3GEYE8JQT7WM",
          "http://www.flipkart.com/steppings-trendy-boots/p/itme96vfhfykfqun?pid=SHOE3S9BYE5XWSKS",
          "http://www.flipkart.com/zoop-c4040pp03-digital-watch-boys-girls/p/itmdg4882bjeetnx?pid=WATDG487YZTHEJZZ",
          "http://www.flipkart.com/carl-3346-1-cheetablue-boots/p/itme32ftfjq5z84a?pid=SHOE32FUXGXGBB5Z",
          "http://www.flipkart.com/zoop-c3030pp05-analog-watch-boys-girls/p/itmdzmr4wekyyx2g?pid=WATDZDSVWQRRGERC",
          "http://www.flipkart.com/pure-source-psi-as-hanggnrlx-relaxing-liquid-air-freshener/p/itme9b8etewsnz73?pid=AIRE9B8EKTNR8J4B",
          "http://www.flipkart.com/peppermint-blues-casual-sleeveless-printed-women-s-top/p/itmebyn5qrndusa8?pid=TOPE5PHFZHVEY42Z",
          "http://www.flipkart.com/xpert-schoolboys-blk-lace-up-shoes/p/itme7djapaayfzrv?pid=SHOE7DJBEPYGQPHF",
          "http://www.flipkart.com/cranberry-club-girl-s-gathered-dress/p/itme9c3ncyfmfgfd?pid=DREE9C3NKTNUCWSN",
          "http://www.flipkart.com/hichkii-casual-cape-sleeve-embroidered-women-s-top/p/itmebtgctdgz9hzf?pid=TOPEBTGCPSWPYGRM",
          "http://www.flipkart.com/clara-certified-katela-3-cts-3-25-ratti-4-prongs-sterling-silver-amethyst-ring/p/itmefp2xquzgwvtx?pid=RNGEFP2XZSFFAGGV",
          "http://www.flipkart.com/prettypataka-party-full-sleeve-woven-women-s-top/p/itme9rcy7vgkykbf?pid=TOPE9RCYS54YZNFG",
          "http://www.flipkart.com/urban-fashion-bank-casual-party-festive-lounge-wear-sleeveless-embellished-women-s-top/p/itme9yrgtky79dcs?pid=TOPEBNGP7UKPXDJD",
          "http://www.flipkart.com/hangover-solid-round-neck-women-s-sweater/p/itmedp5sjnyykkhh?pid=SWTEDP6QUEYGXGDG",
          "http://www.flipkart.com/teemoods-casual-full-sleeve-striped-women-s-top/p/itme45nzgqmgxrpy?pid=TOPE45NZFFUDHKZR",
          "http://www.flipkart.com/ditu-kritu-warrior-aviator-sunglasses/p/itmeabfpgdjbgfmq?pid=SGLEABFPHFPFTNBE",
          "http://www.flipkart.com/claude-lorrain-black-casuals-shoes/p/itme37ctmaac2kz9?pid=SHOE37CTDYFKDJBH",
          "http://www.flipkart.com/gritstones-solid-women-s-track-pants/p/itmds6zeuzrjnbzh?pid=TKPDS6ZEWAR6GTAF",
          "http://www.flipkart.com/gritstones-solid-women-s-track-pants/p/itmds6zecsjhvqhm?pid=TKPDS6ZEWH4KF3SJ",
          "http://www.flipkart.com/gritstones-solid-women-s-track-pants/p/itmds6zeecnvhyjr?pid=TKPDS6ZEQCGBRX9V",
          "http://www.flipkart.com/gritstones-solid-women-s-track-pants/p/itmds6ze3arbeqvh?pid=TKPDS6ZEQBRWSM8U",
          "http://www.flipkart.com/ozel-studio-casual-full-sleeve-printed-women-s-top/p/itme4vr559gav8fv?pid=TOPE4VR5DXAHVAG8",
          "http://www.flipkart.com/teemoods-casual-full-sleeve-striped-women-s-top/p/itme45nzskg4eyw9?pid=TOPEEERRHHZCK8TV",
          "http://www.flipkart.com/nishtaa-yellow-gold-22-k-ring/p/itmdwkzhewvbhw4z?pid=RNGDWKZHDVFQTDYV",
          "http://www.flipkart.com/bownbee-girl-s-gathered-dress/p/itmee9zqhcnwdjbj?pid=DREEE9ZR9THTGUGY",
          "http://www.flipkart.com/fundoo-t-full-sleeve-solid-men-s-sweatshirt/p/itmebhcpdsqznhme?pid=SWSEBHCPAKWKRDPR",
          "http://www.flipkart.com/herberto-girl-s-a-line-dress/p/itmdvf2wquauscyt?pid=DREDVF2W9PTRAEHK",
          "http://www.flipkart.com/cation-casual-3-4-sleeve-solid-women-s-top/p/itme6y8jam9g7a9b?pid=TOPE6Y8JARJNXYBX",
          "http://www.flipkart.com/bells-whistles-striped-round-neck-boy-s-sweater/p/itmed56jt3cuhjd2?pid=SWTED56J4DYNPJDH",
          "http://www.flipkart.com/betty-girl-s-maxi-dress/p/itmedvhxhfz7juym?pid=DREEDVHXJGJWQHVE",
          "http://www.flipkart.com/cation-casual-3-4-sleeve-solid-women-s-top/p/itme2rx99vy5cxgz?pid=TOPE2RX95MBJFRTT",
          "http://www.flipkart.com/yepme-women-flats/p/itmdye2mxuzvebeh?pid=SNDDYE2M83GSMVEJ",
          "http://www.flipkart.com/stilestreet-casual-short-sleeve-solid-women-s-top/p/itmdw7aqzg2fk862?pid=TOPDW7AQKZZHFCZF",
          "http://www.flipkart.com/anaya-women-heels/p/itmeegvmqc4cehya?pid=SNDE8H58SDEBJCFY",
          "http://www.flipkart.com/beebay-girl-s-a-line-dress/p/itmdysnr9qcwaptu?pid=DREDYSNRZGBFFVQ5",
          "http://www.flipkart.com/alibi-casual-short-sleeve-solid-women-s-top/p/itmeegkrawezck7k?pid=TOPE8N26GCA8DNSE",
          "http://www.flipkart.com/vanca-casual-3-4-sleeve-solid-women-s-top/p/itmeatnavgzx2jpg?pid=TOPEATNAAKXFBCCP",
          "http://www.flipkart.com/aaliya-festive-full-sleeve-self-design-women-s-top/p/itmdx9tfy5nxd9xe?pid=TOPDX9TF4PYJMX7B",
          "http://www.flipkart.com/imported-banknote-tester-ball-pen-permanent-alcohol-dye-base-marker/p/itmeevswh3jgqwvm?pid=MAHEEVSWQSZUUFQY",
          "http://www.flipkart.com/autofurnish-car-cover-santro-xing/p/itme3z23xyaz8vwb?pid=CCVE3Z23WWHMGHFY",
          "http://www.flipkart.com/indiano-loafers/p/itmeg52rzjdjgfzf?pid=SHOEG52R2AKHFYHH",
          "http://www.flipkart.com/rainfun-car-cover-800/p/itme6fqugah6ha3w?pid=CCVE6FQUJHNHQVNQ",
          "http://www.flipkart.com/adidas-solid-men-s-track-top/p/itmebgckanmfdahv?pid=TKTEBGCK4ZVWZEZS",
          "http://www.flipkart.com/prime-printed-6-seater-table-cover/p/itmehsmyt9wyhzhf?pid=TCVEHSMY2TNTCKNC",
          "http://www.flipkart.com/prime-printed-8-seater-table-cover/p/itmehsmfvavntx48?pid=TCVEHSMFYEQGRTAZ",
          "http://www.flipkart.com/speedo-men-s-swimsuit/p/itme5gn66mdgtb6n?pid=SWIE5GN6EQ4HKHVD",
          "http://www.flipkart.com/spangel-fashion-audi-style-alloy-mangalsutra/p/itmejpraypptg28z?pid=MNGEJPRAZHS5ZZGA",
          "http://www.flipkart.com/mee-women-s-maternity-panty/p/itmeenemccqsmvag?pid=PANEENEMG9NPM2QQ",
          "http://www.flipkart.com/knp-enterprise-audi-style-alloy-mangalsutra/p/itmejpstpgyzvuzg?pid=MNGEJPST4MZDZCHT",
          "http://www.flipkart.com/asst-full-sleeve-solid-women-s-jacket/p/itme25r8hab6uhyv?pid=JCKE25R8CGBFNJ4H",
          "http://www.flipkart.com/purys-full-sleeve-solid-women-s-fleece-jacket/p/itme2hwfgzskhzuz?pid=JCKE2HWFZD5HZRE5",
          "http://www.flipkart.com/sports-52-wear-men-s-cargos/p/itmeyz52fktjkgjb?pid=CRGEYZ5FGRTYJUT6",
          "http://www.flipkart.com/silver-bucks-camouflage-cargo-men-s-cargos/p/itme5f2szcw33ahv?pid=CRGE5F2RWVWUHYTC",
          "http://www.flipkart.com/basicare-loofah-sponge-rope/p/itmdzjadg2yxf5yt?pid=LFHDBF4BY3PS66NG",
          "http://www.flipkart.com/trufit-full-sleeve-solid-women-s-bomber-jacket/p/itme3x2rzfbtrefk?pid=JCKE3X2R6SBVFZGB",
          "http://www.flipkart.com/sr-crafts-showpiece-15-24-cm/p/itmecpxyfahdrjbf?pid=SHIECPXYNJ8UHGFN",
          "http://www.flipkart.com/transcend-mp-870-8-gb-mp4-player/p/itmcy8t7kpeg3zzf?pid=AUDCY8T7KPEG3ZZF",
          "http://www.flipkart.com/shop-rajasthan-abstract-single-dohar-multicolor/p/itme6znngkbfkbkd?pid=BLAE6ZNNDQZXKCHQ",
          "http://www.flipkart.com/clarks-olga-masie-women-flats/p/itmdpxg6ttkfufgu?pid=SNDDVP9CXEMXNHFS",
          "http://www.flipkart.com/clarks-shavi-loop-women-flats/p/itmdm9j2y4vj959u?pid=SNDDPXG7SGBHW6AF",
          "http://www.flipkart.com/elfani-brilliance-lip-color-127-brick-red-3-5-g/p/itme99ukeqkbh9gx?pid=LSKE99UKDTDN7HBM",
          "http://www.flipkart.com/perfect-women-s-leggings/p/itmehwdvfn2emsmv?pid=LJGEHWDVCNNGPECS",
          "http://www.flipkart.com/vaishna-fashion-women-s-full-coverage-bra/p/itme6zchd8dgffqf?pid=BRAE6ZCHAHQE5HD9",
          "http://www.flipkart.com/florentyne-padded-push-up-bra-women-s/p/itmedx65dpztyaea?pid=BRAEDX65QNAZVKMS",
          "http://www.flipkart.com/luxemburg-bandaeu-women-s-tube-bra/p/itme6mpeayjkxaj4?pid=BRAE6MPEE4X6CMB4",
          "http://www.flipkart.com/laceandme-super-comfort-bandeau-women-s-tube-bra/p/itme7v2uy9gunx7z?pid=BRAE7V2UTY5PYTRT",
          "http://www.flipkart.com/ladyland-mybra-women-s-full-coverage-bra/p/itme7mbpzsrnrzws?pid=BRAE7MBPWCQWDZCZ",
          "http://www.flipkart.com/secret-wish-cherry-print-navy-underwired-women-s-full-coverage-bra/p/itme3wycvdypdcd7?pid=BRAE44SCYYFM74DE",
          "http://www.flipkart.com/ladyland-dia-beige-women-s-full-coverage-bra/p/itme8mx2canxrt6h?pid=BRAE8MX2DNXVEDNH",
          "http://www.flipkart.com/peri-women-s-push-up-bra/p/itmdqzf5gr6hj89y?pid=BRADQZFYHJGCEDV6",
          "http://www.flipkart.com/madaam-nonpadded-women-s-tube-bra/p/itme7y46kqznwptj?pid=BRAE7Y46N7YAFU2H",
          "http://www.flipkart.com/vivity-women-s-full-coverage-bra/p/itmefr6jm4nhhkhe?pid=BRAEFR6JZ6TD2JMY",
          "http://www.flipkart.com/ladyland-daisy-pink-women-s-full-coverage-bra/p/itme8remwvqjbcz8?pid=BRAE8REMHA4XCZH6",
          "http://www.flipkart.com/ladyland-liz-black-bra-women-s-full-coverage/p/itme8mvuhm4c53dp?pid=BRAE8MVUMSMBMNJS",
          "http://www.flipkart.com/ladyland-stellah-women-s-full-coverage-bra/p/itme7mbpay6mhzta?pid=BRAE7MBPXNHC5QHM",
          "http://www.flipkart.com/urbaano-women-s-full-coverage-bra/p/itmeyfdd9mnzs7gd?pid=BRAEYFDEUGF2SWYY",
          "http://www.flipkart.com/oleva-women-s-sports-bra/p/itme2nf6zytckjfz?pid=BRAE2NF6JYPGHQEF",
          "http://www.flipkart.com/younky-fashion-women-s-full-coverage-bra/p/itme3rfcupjcjymy?pid=BRAE3RFCGHJGVJ9Y",
          "http://www.flipkart.com/luxemburg-women-s-tube-bra/p/itme2z9vc8ghgj5u?pid=BRAE2Z9VKVUEJWZQ",
          "http://www.flipkart.com/ladyland-life-women-s-full-coverage-bra/p/itme7fndz2tkemad?pid=BRAE7FNDFAB2PRQD",
          "http://www.flipkart.com/peri-women-s-bra/p/itmdm8dzyffv4zwe?pid=BRADM8DWHUGKNUE7",
          "http://www.flipkart.com/vivity-women-s-full-coverage-bra/p/itmefr6j5as5ggfk?pid=BRAEFR6JFJY6HBWB",
          "http://www.flipkart.com/tia-ten-fashion-women-s-push-up-bra/p/itme6yvwzugzt9kf?pid=BRAE6YVWQJNHHHGG",
          "http://www.flipkart.com/grafion-comfortable-women-s-full-coverage-bra/p/itme3tshehd5zvub?pid=BRAE3TSHYHHD8ZK5",
          "http://www.flipkart.com/vaishna-fashion-women-s-full-coverage-bra/p/itme6z79fxhrkwtz?pid=BRAE6Z79P4B94Y4T",
          "http://www.flipkart.com/floret-women-s-bra/p/itmey7cfwpsskrkk?pid=BRAEY7CD5UFJN9HS",
          "http://www.flipkart.com/florentyne-padded-push-up-bra-women-s/p/itmeeerrwschdrx5?pid=BRAEEERRZPZMPJHK",
          "http://www.flipkart.com/vivity-kfb-24-women-s-plunge-bra/p/itme57ehfabtxqrz?pid=BRAE57EHYXEMH88T",
          "http://www.flipkart.com/urbaano-women-s-full-coverage-bra/p/itmeymfce767vjnm?pid=BRAEYMFCWUSF3U9B",
          "http://www.flipkart.com/luxemburg-women-s-tube-bra/p/itme2m4qzbwqt965?pid=BRAE2M4QWF2FVMH5",
          "http://www.flipkart.com/prettysecrets-fashion-women-s-push-up-bra/p/itme73kfhgjugyrq?pid=BRAE73KF3DUPGFG7",
          "http://www.flipkart.com/peri-women-s-bra/p/itmdusffhv3egt8e?pid=BRADM8DWSRMPPNNX",
          "http://www.flipkart.com/florentyne-women-s-full-coverage-bra/p/itmedz7tedzeycz2?pid=BRAEDZ7TZNFQTXZA",
          "http://www.flipkart.com/florentyne-padded-push-up-bra-women-s/p/itmedx66x9hgct4b?pid=BRAEDX66GWPY6KJ9",
          "http://www.flipkart.com/jsr-paris-beauty-pro-women-s-full-coverage-bra/p/itme3cyxgjetkzxh?pid=BRAE3CYXV4JGWEDA",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jtryyfrfr?pid=BRAEFR6J6SY3F6PS",
          "http://www.flipkart.com/triumph-form-beauty-30-w-women-s-bra/p/itmdwdt5vpxbzhwg?pid=BRADWDT4T8HG5GKV",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jrfmgeg8k?pid=BRAEFR6JZXBQ9NJK",
          "http://www.flipkart.com/grafion-comfortable-women-s-full-coverage-bra/p/itme3tshz2ppjenp?pid=BRAE3TSHYTS4FCU4",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jhhdvyktb?pid=BRAEFR6JYG2HBVSS",
          "http://www.flipkart.com/florentyne-women-s-full-coverage-bra/p/itmedz9g3hqnswhg?pid=BRAEDZ9GVZHWZ5BG",
          "http://www.flipkart.com/hemali-pink-women-s-t-shirt-bra/p/itme5pkzgbmbt4cn?pid=BRAE5PKZBZGYZEMH",
          "http://www.flipkart.com/vaishna-fashion-women-s-full-coverage-bra/p/itme6zcht2qdm9sw?pid=BRAE6ZCHDGWRDHCW",
          "http://www.flipkart.com/tia-ten-stripey-women-s-t-shirt-bra/p/itme5srec7ds6m2r?pid=BRAE5SRETZMB5QYH",
          "http://www.flipkart.com/ladyland-comfy-beige-women-s-full-coverage-bra/p/itme8gb5z9nvszgd?pid=BRAE8GB5JAERH83X",
          "http://www.flipkart.com/luxemburg-strapless-bandaeu-women-s-tube-bra/p/itme3wvqrgdxxyzq?pid=BRAE3WVQHJWKQZHZ",
          "http://www.flipkart.com/ladyland-jenifer-women-s-full-coverage-bra/p/itme7fnd8xbybaux?pid=BRAE7FNDZBHFZFKA",
          "http://www.flipkart.com/ladyland-daisy-purple-women-s-full-coverage-bra/p/itme8smcqnt2xwxc?pid=BRAE8SMCGBASYHKZ",
          "http://www.flipkart.com/laceandme-super-comfort-women-s-stick-on-bra/p/itme7mmgph2qf5xw?pid=BRAE7MMGS2FKH4MJ",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefsfy3kxh2hgt?pid=BRAEFSFYYUGGQTKQ",
          "http://www.flipkart.com/prettysecrets-women-s-t-shirt-push-up-bra/p/itmdwz4jhjjxjqvy?pid=BRADWZ4K9GN5VCM9",
          "http://www.flipkart.com/urbaano-women-s-full-coverage-bra/p/itmeyfdey75mzfpv?pid=BRAEYFDFDG5VFF6K",
          "http://www.flipkart.com/grafion-comfort-feel-women-s-tube-bra/p/itme8rsadu72veh9?pid=BRAE8RSAJKCPQ4WP",
          "http://www.flipkart.com/leading-lady-women-s-full-coverage-bra/p/itmefdmgzj3jggaz?pid=BRAEFDMGHGNN3RQP",
          "http://www.flipkart.com/s4s-comfortable-women-s-full-coverage-bra/p/itmeb2ztg8nm3m3z?pid=BRAEB2ZTZGEU7KZK",
          "http://www.flipkart.com/luxemburg-bandaeu-women-s-tube-bra/p/itme3y3fv9zukxjk?pid=BRAE3Y3FFZGZFKZN",
          "http://www.flipkart.com/luxemburg-women-s-tube-bra/p/itme2z9vpjzgazsj?pid=BRAE2Z9VJ8B8FAD2",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefsfynfzgamdg?pid=BRAEFSFYTXZ4FCDR",
          "http://www.flipkart.com/luxemburg-red-black-pink-color-women-s-tube-bra/p/itme75hseedswcfa?pid=BRAE75HSN6B5RA9V",
          "http://www.flipkart.com/itsmuahlife-dazzle-women-s-full-coverage-bra/p/itmeaqma6zfgpfua?pid=BRAEAQMAYGFHYNTA",
          "http://www.flipkart.com/ladyland-cozy-white-women-s-full-coverage-bra/p/itme8adzvufkwnug?pid=BRAE8AEYGVPNYWG9",
          "http://www.flipkart.com/tia-ten-fashion-women-s-push-up-bra/p/itme6fmz4vg3ys44?pid=BRAE6FMZTRTKVXU6",
          "http://www.flipkart.com/younky-women-s-sports-bra/p/itmey6jxmhstfsvj?pid=BRAEY6JXWCMQ7B5H",
          "http://www.flipkart.com/jsr-paris-beauty-pro-women-s-full-coverage-bra/p/itme3ug9k3d6enne?pid=BRAE3UG9NGHDQZZE",
          "http://www.flipkart.com/sk-dreams-fashion-women-s-full-coverage-bra/p/itme6nzabmz5hvbu?pid=BRAE6NZAQBHWZNMT",
          "http://www.flipkart.com/q-rious-dzire-women-s-full-coverage-bra/p/itme44sub7gjkzdr?pid=BRAE44SUWY4R349F",
          "http://www.flipkart.com/wolfie-lacered117-women-s-push-up-bra/p/itmebb6t3y5hxgac?pid=BRAEBB6TT8GKVG8A",
          "http://www.flipkart.com/younky-women-s-sports-bra/p/itmey6jxfxfhqgz6?pid=BRAEY6JXZJFUHUKZ",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jz3kzhezk?pid=BRAEFR6JZYHZNSGG",
          "http://www.flipkart.com/wolfie-neonbrapeach101-women-s-push-up-bra/p/itmebjbccxfgemfj?pid=BRAEBP5JJA24D2YS",
          "http://www.flipkart.com/younky-non-padded-women-s-full-coverage-bra/p/itme7nmejh8knjyx?pid=BRAE7NMEGDDHG3EX",
          "http://www.flipkart.com/tia-ten-lacy-women-s-push-up-bra/p/itme5vaw4t69x6tq?pid=BRAE5VAWGFY3SGKJ",
          "http://www.flipkart.com/tia-ten-velvetina-women-s-push-up-bra/p/itme5rwp2yzfsn4t?pid=BRAE5RWPQAHEHQDM",
          "http://www.flipkart.com/urbaano-bridal-bra-pack-women-s-full-coverage/p/itmearzhhp8jsnhp?pid=BRAEARZHZU3F3YGY",
          "http://www.flipkart.com/ladyland-liz-women-s-full-coverage-bra/p/itme7fndnqgyjhu6?pid=BRAE7FNDZG77GEZH",
          "http://www.flipkart.com/urbaano-women-s-full-coverage-bra/p/itmeymfd44hszefp?pid=BRAEYMFDYDYVJASW",
          "http://www.flipkart.com/oleva-women-s-full-coverage-bra/p/itme2nf6nwppyrth?pid=BRAE2NF6E8SVUPTD",
          "http://www.flipkart.com/prettysecrets-fashion-women-s-push-up-bra/p/itme73kf4mpggdfb?pid=BRAE73KFJGNSP2NP",
          "http://www.flipkart.com/magiq-zuhi-women-s-full-coverage-bra/p/itme9wnzkwxadstm?pid=BRAE9WNZYBZPXK2X",
          "http://www.flipkart.com/oleva-women-s-full-coverage-bra/p/itme2nf7a6wgnmqu?pid=BRAE2NF7GHGHTURG",
          "http://www.flipkart.com/q-rious-dzire-women-s-full-coverage-bra/p/itme44su3gb27fx3?pid=BRAE44SUCTAAMU87",
          "http://www.flipkart.com/florentyne-padded-push-up-bra-women-s/p/itmedy6vmmdv76gx?pid=BRAEDY6WXTGYRBPP",
          "http://www.flipkart.com/hemali-green-women-s-t-shirt-bra/p/itme5pkz4cbxrfgx?pid=BRAE5PKZGT7AMYZJ",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefukzjheggywm?pid=BRAEFUKZUHFRJGHZ",
          "http://www.flipkart.com/madaam-nonpadded-women-s-tube-bra/p/itme7yf6vmvsew68?pid=BRAE7YF6F8EF7UQB",
          "http://www.flipkart.com/nutex-insaler-women-s-full-coverage-bra/p/itmedgqfhwnkcz5e?pid=BRAEDGQFWPFGVPNF",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefsfzfaghsyvv?pid=BRAEFSFZUEM8Y5DT",
          "http://www.flipkart.com/magiq-nice-merry-women-s-push-up-bra/p/itme8uzgmhagsjfj?pid=BRAE8UZGRKACSJCN",
          "http://www.flipkart.com/ladyland-dia-women-s-full-coverage-bra/p/itme7drsfawvgzzd?pid=BRAE7MBPXVNMGP6M",
          "http://www.flipkart.com/wolfie-polkadotturqoise105-women-s-push-up-bra/p/itmebjhbxyzqgswh?pid=BRAEBKJSNVGDG4DP",
          "http://www.flipkart.com/wolfie-ribbonmaroon118-women-s-push-up-bra/p/itmebb6txrxj7nqa?pid=BRAEBB6TWYYGKYQC",
          "http://www.flipkart.com/tia-ten-comforting-women-s-full-coverage-bra/p/itme6br28gghcdpt?pid=BRAE6BR2Z7YZWPFW",
          "http://www.flipkart.com/ploomz-fashion-women-s-full-coverage-bra/p/itmea5mz6hwdpw2t?pid=BRAEA5MZMPW2UACQ",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jdcgxex4z?pid=BRAEFR6JUMNFA5MT",
          "http://www.flipkart.com/ladyland-bobby-women-s-full-coverage-bra/p/itme7drsq4yf4zgh?pid=BRAE7DRSPHX2WNCU",
          "http://www.flipkart.com/tia-ten-melange-women-s-full-coverage-bra/p/itme6fzqdacqrnwn?pid=BRAE6FZPPGFFGCGH",
          "http://www.flipkart.com/wolfie-neonbrablue103-women-s-push-up-bra/p/itmebjgzvtzwaf4j?pid=BRAEBJGZ6FPZVXVQ",
          "http://www.flipkart.com/wolfie-designred110-women-s-push-up-bra/p/itmebkfhebz2tdrx?pid=BRAEBMWVSDWZYNK8",
          "http://www.flipkart.com/wolfie-neonbrapink102-women-s-push-up-bra/p/itmebjbchvyqh5cd?pid=BRAEBJGPRAZZTECS",
          "http://www.flipkart.com/oleva-women-s-full-coverage-bra/p/itme2nf5gt3hswwj?pid=BRAE2NF6XGU42KGQ",
          "http://www.flipkart.com/peri-women-s-bra/p/itmdm8dzyvwfjzj4?pid=BRADM8DWKXXJDEHW",
          "http://www.flipkart.com/oleva-women-s-full-coverage-bra/p/itme2nf62wcjfcmr?pid=BRAE2NF6QBUFMJTU",
          "http://www.flipkart.com/status-women-s-minimizer-bra/p/itme2gwb2eew2jfd?pid=BRAE2GWB6GSSCFGT",
          "http://www.flipkart.com/younky-fashion-women-s-full-coverage-bra/p/itme3p8yfkyhasxz?pid=BRAE3P8YWVZGNYZH",
          "http://www.flipkart.com/floozy-its-my-choice-women-s-push-up-bra/p/itme8gc4b5kyukpc?pid=BRAE8GC4MJY5ZMYV",
          "http://www.flipkart.com/oleva-women-s-sports-bra/p/itme2nf5hvgt2gyq?pid=BRAE2NF6S2ZYBQWQ",
          "http://www.flipkart.com/vaishna-fashion-women-s-full-coverage-bra/p/itme6z79fzzmydzg?pid=BRAE6Z79C9EBYNGJ",
          "http://www.flipkart.com/vivity-women-s-plunge-bra/p/itmefr6jbskw2gvx?pid=BRAEFR6J5FJ4FUZY",
          "http://www.flipkart.com/jsr-paris-beauty-pro-women-s-full-coverage-bra/p/itme3ug9k3d6enne?pid=BRAE3UG9P8GJXZ2X",
          "http://www.flipkart.com/wolfie-pro-women-s-push-up-bra/p/itmecbxjectkmggk?pid=BRAECBXJJYYERAHY",
          "http://www.flipkart.com/younky-fashion-women-s-full-coverage-bra/p/itme3p8yzsgdkyfs?pid=BRAE3P8YJEQSSANK",
          "http://www.flipkart.com/garfield-casual-short-sleeve-printed-women-s-top/p/itmduetdfgt7pvpk?pid=TOPDUETDZYPSNUMU",
          "http://www.flipkart.com/fashion205-casual-3-4-sleeve-printed-women-s-top/p/itme2k6azncrdngg?pid=TOPE2K6AZC4ZZAJK",
          "http://www.flipkart.com/harpa-casual-sleeveless-solid-women-s-top/p/itme8ayjuzpkagqz?pid=TOPE8AYJV5KUZ6F9",
          "http://www.flipkart.com/sb-retails-sb02-flash/p/itmegp52dz6y5mn3?pid=ACCEGP52WRHFURYZ",
          "http://www.flipkart.com/estilo-sipper-3-450-ml-sipper/p/itmedsenchtvexg5?pid=BOTEDSEN9ZSFUUAQ",
          "http://www.flipkart.com/speedo-monogram-allover-splashback-solid-girl-s/p/itme5gn6azy9a4cn?pid=SWIEHF23HGR3ZRFG",
          "http://www.flipkart.com/omic-poto-blue-1000-ml-sipper/p/itmeemn6n6dddzy4?pid=BOTEEMN6NM57HSBU",
          "http://www.flipkart.com/prachin-varaha-laxmi-sitting-showpiece-11-cm/p/itme3yw8yw7fmzyf?pid=SHIE3YW8AGHPXQZZ",
          "http://www.flipkart.com/disney-minnie-big-head-17-inch/p/itmda5w9yvrgyywf?pid=STFDA3Q4YWEEHH2N",
          "http://www.flipkart.com/sport-silicone-red-swimming-cap/p/itmebfubghyywrcm?pid=SWCEBFUBFYZ9QHKG",
          "http://www.flipkart.com/hitway-lace-up/p/itmeeqnjvxgzxjzz?pid=SHOEEQNJETZKM4PZ",
          "http://www.flipkart.com/bond-beatz-zipper-excellent-sound-wired-headset/p/itmeetkbqybfurag?pid=ACCEETKC9MMAFHTA",
          "http://www.flipkart.com/xerobic-75-cm-gym-ball/p/itmeez2bydkv9tk2?pid=BALEEZ2A4SWPXJU4",
          "http://www.flipkart.com/xerobic-85-cm-gym-ball/p/itmeez2bkwf7xapp?pid=BALEEZ2BZZ3ZT99G",
          "http://www.flipkart.com/shopmantra-che-guevara-revolution-2015-desk-calendar/p/itme34yvhq6z9ga8?pid=CLDE34YVWAJ8ZN6R",
          "http://www.flipkart.com/passion-pragya-women-s-maxi-dress/p/itmeajtkff8ezw4v?pid=DREEAJTKNPH2HBDZ",
          "http://www.flipkart.com/infiniti-red-loafers/p/itme39q6d2kfhjuw?pid=SHOE39Q6PDKHYY2F",
          "http://www.flipkart.com/people-women-s-dress/p/itmeygcy2uzeqneq?pid=DREEYGCXYYZHDGDZ",
          "http://www.flipkart.com/posh-women-s-layered-dress/p/itmdukh45pm5kh7j?pid=DREDUKH4YHWHURG3",
          "http://www.flipkart.com/ten-smart-reds-loafers/p/itme96phguh3gyzg?pid=SHODXQRRGKZ74U9M",
          "http://www.flipkart.com/being-nawab-6-inch-glass-hookah/p/itme62mhhxryya9z?pid=HKHE62MHWS8ANGXU",
          "http://www.flipkart.com/bazaar-pirates-pink-stars/p/itme8zwfvmjc79we?pid=MNKE8ZWFT44GRURB",
          "http://www.flipkart.com/clarks-dunbar-racer-boat-shoes/p/itmdz5ym3zxztyfu?pid=SHODZ5YHTEHZTR3V",
          "http://www.flipkart.com/stylish-step-cross-buckle-loafers/p/itme5qzygprsvwky?pid=SHOE5QZYBEWT53HQ",
          "http://www.flipkart.com/versoba-venetian-roades-loafers/p/itme6pehuwhbhmbr?pid=SHOE6PEHVTQKMYQK",
          "http://www.flipkart.com/urban-monkey-womens-pu-loafers/p/itme2vc3mwg9m7cx?pid=SHOE2VC3UPHYRARN",
          "http://www.flipkart.com/spice-ladies-loafers/p/itme92jkvvd8hyfh?pid=SHOEYVXVYAVXACCW",
          "http://www.flipkart.com/being-nawab-6-inch-glass-hookah/p/itme62mhpp89dzf7?pid=HKHE62MHFXUB85ZE",
          "http://www.flipkart.com/funku-fashion-loafers/p/itmeapt3yskgkdja?pid=SHOEAPT3RUN6RAJ2",
          "http://www.flipkart.com/aptron-premium-manicure-kit-leatherette-case-small/p/itmeygqmzffzmvfk?pid=MNKEYGQMJHGZ4ZRX",
          "http://www.flipkart.com/anaya-16-blue-loafers/p/itmeysukzzqvpkv4?pid=SHOEYSUKSZNTJPJN",
          "http://www.flipkart.com/cubane-wahcb26-loafers/p/itme3mybzngmzq7h?pid=SHOE3MYBTPZVTGYM",
          "http://www.flipkart.com/studio-9-studded-loafers/p/itme96t8cwfbtymf?pid=SHODYGFWEWCG6S88",
          "http://www.flipkart.com/la-briza-vegas-loafers/p/itmefaj5hsmpktjy?pid=SHOEFAJ5NAGQCG8H",
          "http://www.flipkart.com/roha-collections-womens-loafers/p/itme5qezkyhydrp9?pid=SHOE66V8UMNGZKYM",
          "http://www.flipkart.com/funku-fashion-loafers/p/itmeagumepgfu8g9?pid=SHOEAGUMMWFABHUT",
          "http://www.flipkart.com/dizionario-meen111213/p/itmdnw4ajgxjb8xv?pid=MNKDNW49THH74PVT",
          "http://www.flipkart.com/danilo-official-arsenal-fc-2015-wall-calendar/p/itme26u5egshyrnd?pid=CLDE26U5N2TSHREG",
          "http://www.flipkart.com/ruby-sober-047-loafers/p/itme4qfhcsnvs4ku?pid=SHOE4QFHZWCZGCMB",
          "http://www.flipkart.com/prithish-ur-e-best-dad-ever-double-colour-ceramic-mug/p/itme4pxncgkvwbyx?pid=MUGE4PXNXSEFGFZU",
          "http://www.flipkart.com/prithish-crazy-world-gotta-smile-ceramic-mug/p/itmebj7xf3bpvgyf?pid=MUGEBJ7XD5GRWVX8",
          "http://www.flipkart.com/prithish-super-hero-without-cape-ceramic-mug/p/itme99bweh9qpxcf?pid=MUGE99BWHAB47HZC",
          "http://www.flipkart.com/prithish-gemini-black-ceramic-mug/p/itme9hrrm6fhxz3p?pid=MUGE9HRR6HVCRPZT",
          "http://www.flipkart.com/prithish-aries-double-color-ceramic-mug/p/itme9hrrmfj6bn4m?pid=MUGE9HRRXMEBTYR2",
          "http://www.flipkart.com/prithish-oh-crap-she-s-up-ceramic-mug/p/itme6a5huuffckag?pid=MUGE6A5HZUJ924WH",
          "http://www.flipkart.com/prithish-princess-guarded-ceramic-mug/p/itme99bw6xv3kwgg?pid=MUGE99BWGDNEWEN4",
          "http://www.flipkart.com/prithish-aries-black-ceramic-mug/p/itme9hrrncm38xpq?pid=MUGE9HRRWZBDVHZ6",
          "http://www.flipkart.com/prithish-happy-birthday-ceramic-mug/p/itme75zzdbjbfhyy?pid=MUGE75ZZ3G2NGKXZ",
          "http://www.flipkart.com/prithish-man-fix-ceramic-mug/p/itme5hg8vhqwpuf2?pid=MUGE5HG8G63YKHFB",
          "http://www.flipkart.com/prithish-leo-black-ceramic-mug/p/itme9hrrhwjhusqx?pid=MUGE9HRRKMGKHMRT",
          "http://www.flipkart.com/prithish-independence-day-design-9-double-color-ceramic-mug/p/itme9p6dky5gzrkv?pid=MUGE9P6DPPNA4TUS",
          "http://www.flipkart.com/prithish-i-m-mom-what-s-your-superpower-red-blue-bubbles-double-coloured-ceramic-mug/p/itme5pz6awpqv9zh?pid=MUGE5PZ6NQHW7GZY",
          "http://www.flipkart.com/prithish-i-m-mom-what-s-your-superpower-multicoloured-bubbles-black-ceramic-mug/p/itme5pz6cashped3?pid=MUGE5PZ6HEKU5YN8",
          "http://www.flipkart.com/prithish-you-re-one-double-color-ceramic-mug/p/itmebj7x2pngjwfv?pid=MUGEBJ7XKJDMNXY3",
          "http://www.flipkart.com/prithish-magis-believing-yourself-double-color-ceramic-mug/p/itmeawe5hqz45xxe?pid=MUGEAWE5MZRRG5GY",
          "http://www.flipkart.com/prithish-pschedelic-collection-1-ceramic-mug/p/itme92z4zf4jxrpj?pid=MUGE92Z4VKWKGEXX",
          "http://www.flipkart.com/prithish-virgo-ceramic-mug/p/itme9hrravywdazu?pid=MUGE9HRRTTGNEANM",
          "http://www.flipkart.com/prithish-love-dad-father-s-day-ceramic-mug/p/itme6s9ybytwbamn?pid=MUGE6S9YZ25CHZRN",
          "http://www.flipkart.com/prithish-forever-love-you-ceramic-mug/p/itme6syuuqhzbfhh?pid=MUGE6SYUHXASZBRF",
          "http://www.flipkart.com/filtre-roto-pizza-wheel-pizza-cutter/p/itmdznjrdwwy5hp7?pid=PACDZNJRS8AHZVEV",
          "http://www.flipkart.com/3a-autocare-rubber-mat-car-suzuki-new-swift/p/itme83892tf8kakt?pid=CRTE8389ZZJS6W9E",
          "http://www.flipkart.com/purpledip-showpiece-12-cm/p/itmdyzaym5yv3uwf?pid=SHIDYZAYRM4KKJGR",
          "http://www.flipkart.com/voylla-metal-alloy-necklace/p/itmdu4rzurugszz6?pid=NKCDU4RZURUGSZZ6",
          "http://www.flipkart.com/uptown-metal-alloy-necklace/p/itme7mmgfdmju5jj?pid=NKCE7MMGF9C62JPD",
          "http://www.flipkart.com/voylla-precious-simplicity-plain-sterling-silver-chain/p/itme9tbzdkdywrsy?pid=NKCE9TBZD2EGXYJ3",
          "http://www.flipkart.com/vinnis-pretty-please-metal-acrylic-alloy-necklace/p/itmefg3dmngswv9j?pid=NKCEFG3DBZ4EX4SJ",
          "http://www.flipkart.com/vr-designers-acrylic-necklace/p/itmeytxezzjwpcga?pid=NKCEYTXEPHXSXDKM",
          "http://www.flipkart.com/royalscart-kth505-showpiece-33-cm/p/itme8c5ntxcgfbxe?pid=SHIE8C5NBQV5QWCH",
          "http://www.flipkart.com/vinnis-alloy-acrylic-necklace/p/itmdxyfhqyyx83kf?pid=NKCDXYFHHPBSYJDZ",
          "http://www.flipkart.com/apex-rolling-pizza-cutter/p/itme5p38y9khce7t?pid=PACE5P38T4FEUHZC",
          "http://www.flipkart.com/vinnis-pretty-please-metal-acrylic-alloy-necklace/p/itmefg3dwsss5zyj?pid=NKCEFG3DFKHHWBEX",
          "http://www.flipkart.com/womens-trendz-half-jhaler-panadi-thushi-crystal-yellow-gold-plated-alloy-necklace/p/itme3gnv7abay8r8?pid=NKCE3GNVPGUYY8AZ",
          "http://www.flipkart.com/jhondeal-com-wheel-pizza-cutter/p/itmeb7ggu4fbhcw4?pid=PACEB7GGJXVVDZFZ",
          "http://www.flipkart.com/village-handicrafts-aluminum-ceramic-necklace/p/itmefag95dr5fpgh?pid=NKCEFAG9Y7ZHS6M7",
          "http://www.flipkart.com/vinnis-alloy-acrylic-necklace/p/itmdxyfhkkgjvgbd?pid=NKCDXYFHPJ4UNFPU",
          "http://www.flipkart.com/zakaah-jewels-sterling-silver-plated-stone-necklace/p/itmeczjqbr8hmjmu?pid=NKCECZJQS73UZGX3",
          "http://www.flipkart.com/vinnis-pretty-please-metal-acrylic-alloy-necklace/p/itmefg3cyqtqhkyu?pid=NKCEFG3C6TAZNNBY",
          "http://www.flipkart.com/hommate-wheel-pizza-cutter/p/itmedfzpgv2hbdjn?pid=PACEDFZPHQUZ9HET",
          "http://www.flipkart.com/uptown-metal-alloy-necklace/p/itme7mmgqmgbtztp?pid=NKCE7MMGUVXJRFFF",
          "http://www.flipkart.com/aeoss-portable-car-air-vent-mount-mobiles-phones-black/p/itme87c2fgwm5axh?pid=ACCE87C2Q7Y7YARB",
          "http://www.flipkart.com/voylla-metal-alloy-necklace/p/itmdwbpzvrhyzesz?pid=NKCDWBPZEYFAGCW5",
          "http://www.flipkart.com/ndura-tawa-28-cm-diameter/p/itmdxn7bhjgdsyuy?pid=PTPDXN7BGMQBZUTA",
          "http://www.flipkart.com/cookaid-stainless-steel-lid-kadhai-1-2-l/p/itmdvrh4bznhqzh9?pid=PTPDVPEXZACXZW3H",
          "http://www.flipkart.com/tosiba-kadhai-500-ml/p/itmeangbjnndg7ug?pid=PTPEANGB8CAX4YKW",
          "http://www.flipkart.com/gear-x-sports-mount-2/p/itmdzy2489csvvsq?pid=ACCDZY24EZN3T4DU",
          "http://www.flipkart.com/hawkins-futura-hard-anodized-deep-fry-pan-7-5-l-360-mm-kadhai/p/itmdvrh4wskwjgfs?pid=PTPDVPEXFUZNDZZH",
          "http://www.flipkart.com/pigeon-gravy-premium-lid-kadhai-6-l/p/itmdvrh5uhzghtbt?pid=PTPDVPEXYZGYEEFG",
          "http://www.flipkart.com/ambitione-car-holder/p/itme93zdehemsqnj?pid=ACCE93ZDRDSJD3RG",
          "http://www.flipkart.com/bestech-kadhai-4-l/p/itmdzy9jhpf53gky?pid=PTPDZY9JW3HSEPWC",
          "http://www.flipkart.com/sygtech-windshield-car-cradle-mount-phone-holder-samsung-s5/p/itme2wc8kgg47kbh?pid=ACCE2WC8KXAKMNAF",
          "http://www.flipkart.com/trinketbag-red-tie-alloy-necklace/p/itmduvk2cujqhrfk?pid=NKCDUYA5RGAGR4PY",
          "http://www.flipkart.com/villcart-brass-bail-gadi-showpiece-5-5-cm/p/itmdyzaggcbkgggq?pid=SHIDYZAGTXAHCJ4G",
          "http://www.flipkart.com/swethamber-arts-brass-musical-lady-set-4-statue-showpiece-7-cm/p/itmeccmnhjtbcpus?pid=SHIECCMNHQD5SZPZ",
          "http://www.flipkart.com/vtc-thumb-up-mobile-stand-pink/p/itmebezzzkegepzj?pid=ACCEBEZZEQZ3SSAZ",
          "http://www.flipkart.com/cookaid-stainless-steel-lid-kadhai-1-2-l/p/itmdvrh4hkmx5mbq?pid=PTPDVPEXSANDVSJQ",
          "http://www.flipkart.com/disney-cars-customs-traditional-pinata/p/itmdpucdvdebzggf?pid=PITDPPMDFRXXQGNX",
          "http://www.flipkart.com/aeoss-bike-phone-support-mobile-holder/p/itme8c3ykrgtymwg?pid=ACCE8C3YU6JDREMH",
          "http://www.flipkart.com/leo-natura-paniarakkal-7-hole-kadhai-na-l/p/itmeycf7sv957kbz?pid=PTPEYCF7GZU2T54E",
          "http://www.flipkart.com/thegudlook-self-design-women-s-muffler/p/itmeygfhz5auscnh?pid=MFLEYGFH8PFBVRDG",
          "http://www.flipkart.com/dailyware-kadhai-1-5-l/p/itmdzycehfschgtz?pid=PTPDZYCE2H35GHG4",
          "http://www.flipkart.com/peach-3mm-premium-green-pan-kadhai-2-5-l/p/itmeb88uthth4y3m?pid=PTPEB88UTZRHHVXD",
          "http://www.flipkart.com/chefkraft-tri-ply-kadhai-3-2-l/p/itme2ssxwxzsxhq9?pid=PTPE2SSXSTFH6HYY",
          "http://www.flipkart.com/uptown-metal-alloy-necklace/p/itme7mmgsn8ughwy?pid=NKCE7MMGGHXSGDBC",
          "http://www.flipkart.com/alda-wok-glass-lid-kadhai/p/itmdvrh4fz9fcfex?pid=PTPDVPEXAA854NEY",
          "http://www.flipkart.com/voylla-cubic-zirconia-fabric-necklace/p/itmdzhf7b9vjkg2c?pid=NKCDZHF7J4GGHHSG",
          "http://www.flipkart.com/pigeon-triply-kadhai-2-l/p/itme34yjdmug2yn2?pid=PTPE34YJXKXZVTWK",
          "http://www.flipkart.com/crafts-house-showpiece-6-5-cm/p/itme5hz5xjkkgbgh?pid=SHIE5HZ5UWWXYXWV",
          "http://www.flipkart.com/jaipan-kd2-5-kadhai-2-5-l/p/itme5wb8zwgaecrg?pid=PTPE5WB8Z2C6YYCQ",
          "http://www.flipkart.com/urthn-alloy-necklace/p/itmdyrhg63uth3cz?pid=NKCDYRHGP2UFXMT7",
          "http://www.flipkart.com/retina-1-mobile-holder-car-charger-usb-cable-combo/p/itmeasgphs7fhuxr?pid=AVCEASGPSFXKFXB8",
          "http://www.flipkart.com/village-handicrafts-alloy-necklace/p/itmefag9gnmrsyqk?pid=NKCEFAG9TAF3VAFY",
          "http://www.flipkart.com/united-kadhai-na-l/p/itme2gjqm6uwcyy8?pid=PTPE2GJQXEWHGZEK",
          "http://www.flipkart.com/vr-designers-glass-necklace/p/itmdwryfvnvzcxw5?pid=NKCDWRYFPAFEQA5Z",
          "http://www.flipkart.com/purpleyou-cotton-embroidered-blouse-material/p/itme88mh9kqd2gbf?pid=FABE88MGUBPCQWR8",
          "http://www.flipkart.com/total-agency-car-mobile-stand-holder-mount/p/itme9eyrtxhkyhje?pid=ACCE9EYRRNZYZUBG",
          "http://www.flipkart.com/vinnis-style-diva-metal-acrylic-alloy-necklace/p/itmefg3cyb8gzzvm?pid=NKCEFG3CHGEHMRTD",
          "http://www.flipkart.com/3a-autocare-3d-mat-car-suzuki-new-swift/p/itme8389ww5htxg6?pid=CRTE8389HNP2UHPT",
          "http://www.flipkart.com/imported-long-lazy-mobile-holder-stand/p/itmey6jytc9zhamy?pid=ACCEY6JYDGGESWXC",
          "http://www.flipkart.com/cookaid-stainless-steel-lid-kadhai-1-2-l/p/itmdvrh4zncgthgm?pid=PTPDVPFYEKTVFEZ8",
          "http://www.flipkart.com/fly-mini-clip-mobile-holder/p/itmefet7fkedyzrs?pid=ACCEFET7MKNAJVAH",
          "http://www.flipkart.com/woodino-handicrafts-showpiece-6-5-cm/p/itme2cajptz3dzf7?pid=SHIE2CAJP6XBWPU2",
          "http://www.flipkart.com/r-s-jewels-handmade-decoretive-designs-iron-pot-vase-showpiece-76-cm/p/itmef8dujhsexqyw?pid=SHIEF8DUHZJP8MVC",
          "http://www.flipkart.com/fly-universal-mobile-holder-crystal-car-windshield/p/itmdrrehjsxc8ey9?pid=ACCDRREFMB99QZ42",
          "http://www.flipkart.com/urdiva-fashions-metal-necklace/p/itmecjahtmvyg9hw?pid=NKCECJAHAMVG7Q8M",
          "http://www.flipkart.com/bracketron-tour-window-hip-kicker/p/itme2sxdry2gfz6f?pid=ACCE2SXDBTYNYYQ3",
          "http://www.flipkart.com/mom-italy-wheel-pizza-cutter/p/itmdztd7xyqhzcze?pid=PACDZTD7YB2EUMYE",
          "http://www.flipkart.com/vr-designers-metal-necklace/p/itmeygtgh5m6hefh?pid=NKCEYGTG972MN8T3",
          "http://www.flipkart.com/hawkins-futura-hard-anodized-kadhai-2-5-l/p/itmdvrh4a6y6yf7f?pid=PTPDVPEXXGZQMC2G",
          "http://www.flipkart.com/urthn-alloy-necklace/p/itmdyrhguzuztg22?pid=NKCDYRHGHJCQ65WW",
          "http://www.flipkart.com/voylla-yellow-gold-plated-fabric-necklace/p/itmdy8s8vzzhrrqq?pid=NKCDY8S8CCG32GQH",
          "http://www.flipkart.com/suruchi-kadhai-1-l/p/itme7jzcjc67schs?pid=PTPE7JZCBGGKPSGS",
          "http://www.flipkart.com/funku-fashion-women-heels/p/itmehzkgcmjh5jzy?pid=SNDEHZKGKGHDFG57",
          "http://www.flipkart.com/funku-fashion-women-heels/p/itmehzkg4fh8ykcs?pid=SNDEHZKGZHHHQVYX",
          "http://www.flipkart.com/being-trendy-quit-x-ego-twist-ce-5-automatic-electronic-cigarette/p/itmef7mgnfysa6mx?pid=ECIEF7MGVGZAZMGG",
          "http://www.flipkart.com/hangrr-premium-single-breasted-solid-men-s-suit/p/itme5gt38hmxgvgf?pid=SUIE5GT3DSJCKEJF",
          "http://www.flipkart.com/brahaan-blue-tag-single-breasted-solid-men-s-suit/p/itme8h94jzzyghht?pid=SUIE8H94SYGX7PKR",
          "http://www.flipkart.com/desert-eshop-real-antique-brass-royal-3-minute-sand-timer-281-showpiece-7-cm/p/itme86xatmpqyahg?pid=SHIE86XAGBVWRWH3",
          "http://www.flipkart.com/elephant-9-84-inch-lid/p/itmdvhugevarpwb8?pid=LIDDVFAFGAYTM8HH",
          "http://www.flipkart.com/equinox-eb-eq-33-body-fat-analyzer/p/itmdsqhjmfhzhmug?pid=BFAD3ZJYYCXDAVGH",
          "http://www.flipkart.com/nihar-pirangi-bomber-showpiece-10-cm/p/itme8m9p6bddjb2d?pid=SHIE8M9PWUF5H4SF",
          "http://www.flipkart.com/intel-3-2-ghz-lga-1150-i5-4460-bx80646i54460-processor/p/itmefbqmfr7n6her?pid=PSREFBQM8V7GVCGX",
          "http://www.flipkart.com/diovanni-fashionable-monochrome-metal-alloy-necklace/p/itmdqsvdqwph2zzy?pid=NKCDQSVCY7GJM39D",
          "http://www.flipkart.com/bagru-crafts-wall-hanging-lord-ganesha-showpiece-21-69-cm/p/itme954fm8ebqtx7?pid=SHIE954FZSSHYFGG",
          "http://www.flipkart.com/intel-1-8-ghz-lga-1155-celeron-g460-processor/p/itmd7nkjuehd5uzy?pid=PSRD7NKJGFMGAZQG",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdtaxfef5bxf4s?pid=NKCDTAXFFYUASQNQ",
          "http://www.flipkart.com/giftwallas-crystal-necklace/p/itmefkbydugv5kez?pid=NKCEFKBYZBXUBYBZ",
          "http://www.flipkart.com/leoxsys-leo-150n-3g-ad/p/itmdp2mybc8qzxy2?pid=RTRDP2HXHPPTGQHE",
          "http://www.flipkart.com/nike-combo-set/p/itmds6vefbx5x7yq?pid=CAGDS6VEGGYYEYUH",
          "http://www.flipkart.com/fayon-golden-tassel-alloy-necklace/p/itmdyyqwgchfqmf6?pid=NKCDYYQWT2ZZUYZD",
          "http://www.flipkart.com/netgear-r6220-ac1200-dual-band-gigabit-wi-fi-router/p/itme8gjuaxyayhtt?pid=RTRE8GJUFNETVUMZ",
          "http://www.flipkart.com/tenda-3g150b/p/itmdngvvqpqy9gpz?pid=RTRDNGVMCHXQT6HU",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdtax242mtjgep?pid=NKCDTAXFFDCCGUY4",
          "http://www.flipkart.com/playboy-london-combo-set/p/itme4bqyhu4zzafq?pid=CAGE4BQYUXBFXZVF",
          "http://www.flipkart.com/monet-passport-gift-set-combo/p/itme7gufuwbyqsrx?pid=CAGE7GUFJG7JZ3HC",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdrdwbskkwpn9k?pid=NKCDRDWANFDGXSSK",
          "http://www.flipkart.com/cinthol-deo-spray-dive-pack-2-combo-set/p/itmdw63hy6prz9hf?pid=CAGDW63HYZAJ4EK9",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4agmxakcs?pid=NKCE4VA4M7ZHQFV6",
          "http://www.flipkart.com/intex-w150d/p/itme7ft9d98cccgs?pid=RTRE7FT9VKRGNTRR",
          "http://www.flipkart.com/pinnakle-dual-compartment-utility-pouch-v4-printed-art-resin-pencil-box/p/itme7yyyaczptgrv?pid=PBXE7YYYSETDYV9P",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme3y5peqnjex9r?pid=NKCE3Y5PSKAJSBPY",
          "http://www.flipkart.com/asus-rt-n13u-b1-wireless-n-all-in-one-printer-server-router/p/itmd3849zu3sgwxq?pid=RTRD38494HWZVMAK",
          "http://www.flipkart.com/tenda-3g611r/p/itmdp2cmwkrc3smw?pid=RTRDNGVMH2ZJZRMQ",
          "http://www.flipkart.com/adidas-ice-drive-dynamic-pulse-combo-set/p/itme6hyjfrby89yv?pid=CAGE6HYJPDEM4AN3",
          "http://www.flipkart.com/goldnera-alloy-necklace/p/itmdxzguwhyfztbs?pid=NKCDXZGUZKNYVXG9",
          "http://www.flipkart.com/asus-rt-n14uhp-high-power-wireless-n300-3-in-1-router-ap-range-extender/p/itmdu88akqfrzu2u?pid=RTRDU88AKQFRZU2U",
          "http://www.flipkart.com/etti-esj69-multi-glass-necklace/p/itme96sxwwddupaw?pid=NKCE96SXVSQHFGNP",
          "http://www.flipkart.com/tp-link-tl-mr3420-3g-4g-wireless-n-router/p/itmebxpfywhy4k4y?pid=RTRDET9AQR7EMM2G",
          "http://www.flipkart.com/playboy-hollywood-malibu-combo-set/p/itme4bqxh8th3mes?pid=CAGE4BQXKEZPSHWG",
          "http://www.flipkart.com/belkin-play-max-modem-router/p/itmdffystcgaxnhb?pid=RTRDFFYGTZUBKJTS",
          "http://www.flipkart.com/adidas-champions-league-combo-set/p/itme6gqcptaf9pzg?pid=CAGE6GQCC6YG7FTD",
          "http://www.flipkart.com/asus-wireless-ac2400-dual-band-gigabit-router/p/itmeyty3qxhanrze?pid=RTREYTY2TMVNXZG4",
          "http://www.flipkart.com/netgear-wndr3700-n600-dual-band-wireless-gigabit-router/p/itmdwevazvtduqej?pid=RTRDFFYGJ4GNRSHQ",
          "http://www.flipkart.com/tenda-te-4g302/p/itmdzk8xhju289fn?pid=RTRDZK8XZBQDJ35U",
          "http://www.flipkart.com/huawei-ws331c-300-mbps-wireless-range-extender/p/itmefwynghabx2m4?pid=RTREFWYNH9RGDCQK",
          "http://www.flipkart.com/anna-andre-paris-red-horizon-majesty-deodorant-combo-set/p/itme22eewkerfhmt?pid=CAGE22EEH2JMZFZV",
          "http://www.flipkart.com/armaf-shades-combo-set/p/itme9agrhmsae3fj?pid=CAGE9AGRUGPHV5FM",
          "http://www.flipkart.com/trendnet-tew-752dru/p/itme3kkxhagvzjtw?pid=RTRE3KKX5RWCKMHH",
          "http://www.flipkart.com/netgear-wn2500rp-universal-dual-band-wi-fi-range-extender/p/itmdzcpcdjw8gcxg?pid=RTRDZCPAY9YHMG4X",
          "http://www.flipkart.com/tenda-w308r/p/itmdngvvxgtmfwwj?pid=RTRDNGVMKKUNBA5B",
          "http://www.flipkart.com/edimax-br-6428nc/p/itmdzbj55hg9baw2?pid=RTRDZBJ5VAZG7VGC",
          "http://www.flipkart.com/goldnera-brass-chain/p/itmdypdsfyxubada?pid=NKCDYPDSUPDSVYU3",
          "http://www.flipkart.com/goldnera-brass-chain/p/itmdypdschgfjhh2?pid=NKCDYPDS8THDBS7K",
          "http://www.flipkart.com/park-avenue-cool-blue-good-morning-pack-2-deodorants-combo-set/p/itmdtsjufvmvp3xg?pid=CAGDTSJUFVMVP3XG",
          "http://www.flipkart.com/zyxel-pla4231-500-mbps-powerline-wireless-n-extender-single-pack/p/itmef5vhgyg3ef8r?pid=RTREF5VHQR3VGVHY",
          "http://www.flipkart.com/asus-dsl-ac68u-dual-band-wireless-ac1900-vdsl-adsl-modem-router/p/itmefh84edgfmsqm?pid=RTREFH7UGSFUT6PB",
          "http://www.flipkart.com/klassik-animal-random-art-card-board-pencil-box/p/itme7nyscyrwkwwq?pid=PBXE7NYSPF4FKVY6",
          "http://www.flipkart.com/iball-wireless-n-router/p/itmdz87gbp7tddm9?pid=RTRDZ5PJTSHHXGME",
          "http://www.flipkart.com/d-link-dir-816l/p/itme2rmajccgndpj?pid=RTRE2RMAAU4D3H5X",
          "http://www.flipkart.com/asus-rt-ac68u-dual-band-wireless-ac1900-gigabit-router/p/itmdrdpr7q935k2s?pid=RTRDRDPR9JHCSBGH",
          "http://www.flipkart.com/tenda-f3-300mbps-wireless-router-3-fixed-antenna-3lan-1wan-port/p/itmebg9ccwkmt4zs?pid=RTREBG9CJ7HHSHGJ",
          "http://www.flipkart.com/tp-link-tl-wr941nd-300mbps-wireless-n-router/p/itmd8fnghsbckk6z?pid=RTRD8FNGHSBCKK6Z",
          "http://www.flipkart.com/asus-rt-n12-lx-300mbps-wireless-router/p/itmd6354btvnrxtz?pid=RTRD6352VX7RZSWG",
          "http://www.flipkart.com/alex-s-barbie-series-doll-art-plastic-pencil-box/p/itmebyhcq7z3zjdy?pid=PBXEBYHC7D4NF76E",
          "http://www.flipkart.com/trendnet-n150-wireless-adsl-2-modem-router/p/itmdqzz3thdxphdv?pid=RTRDQZMJBWHZCXZT",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmefmkxgdny9nz5?pid=NKCEFMKXRPRZAZKK",
          "http://www.flipkart.com/beverly-hills-polo-club-combo-set/p/itmdrjj4aaypx5ab?pid=CAGDRJJ3HWPMJUCC",
          "http://www.flipkart.com/outshiny-eagle-printed-art-polyester-pencil-box/p/itme4rb4zzybu3y4?pid=PBXE4RB4DSFQPASY",
          "http://www.flipkart.com/kamasutra-combo-offer-pack-set/p/itmdzvamptyzywv6?pid=CAGDYY25E8RVC7EG",
          "http://www.flipkart.com/tenda-a5/p/itmdp2cxeq633zhd?pid=RTRDNY65WHG9FHTS",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4a3ehpjd2?pid=NKCE4VA4SEQFEYUH",
          "http://www.flipkart.com/etti-esj72-multi-glass-necklace/p/itme96sxv9zucgkk?pid=NKCE96SXDK3JFZC3",
          "http://www.flipkart.com/d-link-dir-816-wireless-ac750-dual-band-router/p/itme3xwgmuvqzbhp?pid=RTRE3XW7JS6YJHG5",
          "http://www.flipkart.com/nivea-happy-time-pack-2-combo-set/p/itmdrj8wgutgzq2y?pid=CAGDRJ8WYSTGZ6UE",
          "http://www.flipkart.com/www-thepaper-asia-floral-art-canvas-leather-pencil-box/p/itmeaen4q9r6jtcr?pid=PBXEAEN4R6HUGZJV",
          "http://www.flipkart.com/netis-wf2412/p/itmdmtetvcghpxdc?pid=RTRDMTEPMWHHPSUS",
          "http://www.flipkart.com/d-link-dir-810l/p/itmdqgv4rasepvrc?pid=RTRDQGV3ZTKAZTPD",
          "http://www.flipkart.com/iball-ib-w4gx150n-4g-wireless-n-router/p/itme63npz55yrzzu?pid=RTRE63NMMRZ8MUJT",
          "http://www.flipkart.com/tp-link-td-w8960n/p/itmeax3dxegbzbvz?pid=RTREAX3DGDRSSYFT",
          "http://www.flipkart.com/fayon-red-chic-alloy-necklace/p/itmdv7kgwzhqbznn?pid=NKCDV7KGEEZHJVJY",
          "http://www.flipkart.com/arabian-nights-evolve-combo-set/p/itme4b8fekhhxet7?pid=CAGE4B8YHZK3KTUX",
          "http://www.flipkart.com/park-avenue-alpha-combo-set/p/itmdwgcyyggzu4qw?pid=CAGDWGCSDGYNDH3Y",
          "http://www.flipkart.com/netgear-jnr3210-n300-wireless-gigabit-router/p/itmdekmqgbfrcdqm?pid=RTRDEKJVRCDYXRST",
          "http://www.flipkart.com/d-link-dwr-111-3g-router-wan-auto-failure/p/itmdtsbqw94hj8vt?pid=RTRDTSBQW94HJ8VT",
          "http://www.flipkart.com/adidas-get-ready-natural-vitality-combo-set/p/itme6hyj3zqgm3dn?pid=CAGE6HYJGDZQXHQD",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdudg8tbqxea2d?pid=CAGDUDG8TBQXEA2D",
          "http://www.flipkart.com/nike-up-down-combo-set/p/itme8tq8zwe9psnj?pid=CAGE8TQ8KFEGHY9M",
          "http://www.flipkart.com/edimax-ar-7286wna/p/itmdzbj5kxzg7dnv?pid=RTRDZBJ5E8TBFDD9",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdv2545ja7mjdz?pid=CAGDV253CTVNMSP2",
          "http://www.flipkart.com/belkin-share-modem-n-router/p/itmdffysaqegsqyg?pid=RTRDFFYGM2TEWVCC",
          "http://www.flipkart.com/engage-combo-set/p/itmdu84g2g5aeae5?pid=CAGDU84G2G5AEAE5",
          "http://www.flipkart.com/fashblush-forever-new-blackbead-alloy-necklace/p/itme676xz8ffwbkq?pid=NKCE676XRFECGZHC",
          "http://www.flipkart.com/asus-wireless-n150-adsl-modem-router/p/itmdyr4gvnn7wgha?pid=RTRDYR4HXQJ8T3WR",
          "http://www.flipkart.com/belkin-wireless-dual-band-travel-router/p/itmdetbdenggzqj8?pid=RTRDETBCHYE3UZAA",
          "http://www.flipkart.com/asus-rt-n12-d1-router/p/itmdrmgyhdgqgfce?pid=RTRDRMGYGV73A3XJ",
          "http://www.flipkart.com/tenda-te-fh1202-wireless-high-power-ac1200-dual-band-gigabit-wifi-router/p/itme7dbhtarjj5pk?pid=RTRE7DBHH85JTHXC",
          "http://www.flipkart.com/asus-rt-n12c1-router/p/itmdztfczxcrzjj8?pid=RTRDZTF9URF2UFPF",
          "http://www.flipkart.com/wd-my-net-n900-hd-dual-band/p/itmdf7qutnznsqdu?pid=RTRDF7QU6QFFZFKB",
          "http://www.flipkart.com/netgear-wnr614-wireless-n300-router/p/itmdyjungp3eueqa?pid=RTRDYJUN75ZHEUD4",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdtax2cgdm4qcf?pid=NKCDTAXFQMHPMUTQ",
          "http://www.flipkart.com/apple-airport-express-base-station-wireless-router/p/itmdqsshs3cwmums?pid=RTRDQSSHGP7UGRFC",
          "http://www.flipkart.com/park-avenue-good-morning-iq-pack-2-deodorants-combo-set/p/itmdtsjunhzgyzrs?pid=CAGDTSJUNHZGYZRS",
          "http://www.flipkart.com/kolkata-knight-riders-combo-set/p/itmeyfzwmgzywtqu?pid=CAGEYFZWNWG6SMHG",
          "http://www.flipkart.com/tp-link-tl-wa750re/p/itmdy9nvzyztgrmf?pid=RTRDY9NVKBBNGYMU",
          "http://www.flipkart.com/anna-andre-paris-majesty-deodorant-combo-set/p/itme22eebsxqbnmh?pid=CAGE22EETSQPZKZA",
          "http://www.flipkart.com/tp-link-archer-c20i-ac750-wireless-dual-band-router/p/itme387p98scw9gh?pid=RTRE387ZDKW7NQGV",
          "http://www.flipkart.com/disney-cinderella-cartoon-art-metal-pencil-box/p/itme7w3agcakzagk?pid=PBXE8FW6ZZZF2RQA",
          "http://www.flipkart.com/nike-combo-set/p/itme44j5rhyethhq?pid=CAGE44J5NGQHXMHF",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdrdwbbwhzgbzw?pid=NKCDRDWAZU9ZJNHZ",
          "http://www.flipkart.com/cinthol-deo-spray-intense-energy-play-combo-set/p/itme7tvzaztv9q8e?pid=CAGE7TVZGNX4AMDR",
          "http://www.flipkart.com/aoc-pencil-pouch-polka-dots-art-cloth-box/p/itme6zckpdfu6kgg?pid=PBXE6ZHNEGF3VGZW",
          "http://www.flipkart.com/adidas-pure-lightness-combo-set/p/itme6gqczzzz2cyd?pid=CAGE6GQC6UYAGC5C",
          "http://www.flipkart.com/lava-w520-3g-router/p/itmdhwzfsrjxwycv?pid=RTRDHWZYK9SN4MGZ",
          "http://www.flipkart.com/asus-rt-n66u-dual-band-wireless-n900-gigabit-router/p/itmd7xkf2ga7f2an?pid=RTRD7XKFDBPBR6CV",
          "http://www.flipkart.com/trendnet-n150-wireless-router/p/itmdqzz3rxrgtfn2?pid=RTRDQZMJHRSR6CA9",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme3y5pubghrmb8?pid=NKCE3Y5PHMWUUWQ3",
          "http://www.flipkart.com/wild-stone-deo-offer-combo-set/p/itmdr3xhtcvacscs?pid=CAGDR3XKFCZ6XA2F",
          "http://www.flipkart.com/tp-link-tl-wr841hp-300-mbps-high-power-wireless-n-router/p/itme38hhftnp3kze?pid=RTRE38HFGYDDZYGZ",
          "http://www.flipkart.com/engage-trail-blush-combo-set/p/itmdvvyfvh9k577x?pid=CAGDVVX954JSSCGP",
          "http://www.flipkart.com/belkin-basic-n150-router/p/itmdg5cryc3b3j5c?pid=RTRDFFYG65VG5RWS",
          "http://www.flipkart.com/netis-wf2419/p/itmecfhxgnzth4xq?pid=RTRECFHX3TDFD9SP",
          "http://www.flipkart.com/iball-ib-wrx300np-300-mbps-extreme-high-power-wireless-n-router/p/itme4zqbdxz368cy?pid=RTRE4ZQB3BTTWZKT",
          "http://www.flipkart.com/tenda-f303-wireless-n300-easy-setup-router/p/itme4vnchtcsduhv?pid=RTRE4VNCJZ3UPGQZ",
          "http://www.flipkart.com/comfast-cf-wr500n/p/itmdrsbwgpmeduse?pid=RTRDRSBNRDBZEPTY",
          "http://www.flipkart.com/huawei-ws319-300-mbps-wireless-n-router/p/itme96w3pwwxzgtj?pid=RTRE96W36WAJHRCF",
          "http://www.flipkart.com/tp-link-tl-wr702n-150mbps-wireless-n-nano-router/p/itmdtp8datbmzzhw?pid=RTRDB8GKEGG5E3XG",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4uarzdxm3?pid=NKCE4VA49YHSX6KW",
          "http://www.flipkart.com/iball-150m-extreme-wireless-n-router/p/itmddh2gu2ydspfr?pid=RTRECM6WZFBZYSTK",
          "http://www.flipkart.com/asus-dsl-n10e-wireless-n150-adsl-modem-router/p/itmd7xkfs6hyzmnq?pid=RTRD7XKFRCZH8TE4",
          "http://www.flipkart.com/neo-gold-leaf-fancy-school-art-plastic-pencil-box/p/itmeacg2d7ghgzb6?pid=PBXEACG2FBGPQKWG",
          "http://www.flipkart.com/denver-deodorant-no-13-gift-set-combo/p/itme53fsbmfaupzb?pid=CAGE53FSKAYSFUXG",
          "http://www.flipkart.com/zero-gravity-pack-combo-set/p/itme4dwqzvkfdqxm?pid=CAGE4DWQQYHVPD8C",
          "http://www.flipkart.com/anna-andre-paris-set-treasure-red-horizon-deodorants-160ml-each-combo/p/itme5rnepsztq5yh?pid=CAGE5RNE4JVBXZBX",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4cmfvzfrm?pid=NKCE4VA4M2ZKZGUY",
          "http://www.flipkart.com/linksys-re2000-wireless-range-extender-n300-dual-band/p/itmdq9yzvbzybeh3?pid=RTRDQ9YMUHW7PYYE",
          "http://www.flipkart.com/tenda-a6/p/itmdngvv3dzzxf8g?pid=RTRDNGVME4HGYAM8",
          "http://www.flipkart.com/iball-300m-wireless-n-adsl2-3g-router/p/itmdypa4qdnajg22?pid=RTRDYPA4PJHCJCGF",
          "http://www.flipkart.com/engage-urge-mate-combo-set/p/itmdvvyfx9yddr8u?pid=CAGDVVX97KZEH2EJ",
          "http://www.flipkart.com/real-madrid-no-7-gift-set/p/itmdzvgt7qhaayny?pid=CAGDZVGTV3SMMMBY",
          "http://www.flipkart.com/playboy-london-berlin-combo-set/p/itme4bqxhpshykgg?pid=CAGE4BQXSJPTBUS4",
          "http://www.flipkart.com/alex-s-mickey-mickey-donald-duck-art-plastic-pencil-box/p/itmebyhccms7g4nu?pid=PBXEBYHC4S5BQYDA",
          "http://www.flipkart.com/tp-link-tl-mr3220-3g-4g-wireless-n-router/p/itmeyfznjadytdmx?pid=RTRD8FNG6FUTFZQJ",
          "http://www.flipkart.com/tenda-te-d820r/p/itmdzk8xtdvypegz?pid=RTRDZK8XDZTJDJFN",
          "http://www.flipkart.com/engage-combo-set/p/itmdunh3rsmjgkb8?pid=CAGDUNH3FHZWCVKN",
          "http://www.flipkart.com/spinz-combo-set/p/itme38d7f66drqjm?pid=CAGE38D7F5XQSYNC",
          "http://www.flipkart.com/tenda-n60/p/itmdngvvwgqtyxyx?pid=RTRDNGVMSXKSREUJ",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmefmkxay4vkne7?pid=NKCEFMKXMH4AX4WF",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme3y5pvfhuhttn?pid=NKCE3Y5PDN4U66HC",
          "http://www.flipkart.com/benetton-lets-love-moov-gift-set-combo/p/itme75zxb2qsmasc?pid=CAGE75ZXGZPBMZVG",
          "http://www.flipkart.com/onnet-3000ocurro-3g-wifi-router/p/itme2xjsshuhd3ew?pid=RTRE2XJSG2ZFVFTW",
          "http://www.flipkart.com/isun-isn-v01/p/itme6cpuyvdezhuf?pid=RTRE6CPUD2WJRNMG",
          "http://www.flipkart.com/etti-esj27-multi-crystal-glass-necklace/p/itme8juj8yezc6zu?pid=NKCE8JUJEUE3HR4H",
          "http://www.flipkart.com/asus-rt-n14u-wireless-n300-cloud/p/itmdhy5kaenwhhng?pid=RTRDHYYVPHSGSDGA",
          "http://www.flipkart.com/indian-charm-glass-necklace/p/itme8rb58h8zhwzv?pid=NKCE8RB5BFGQYK4G",
          "http://www.flipkart.com/lava-w200-3g-router/p/itmdk7ufm6ggtppx?pid=RTRDK7TWJB6RCNP9",
          "http://www.flipkart.com/junk-glass-necklace/p/itme34thqrcu7muz?pid=NKCE34THCPW5V7FV",
          "http://www.flipkart.com/vincent-valentine-paris-set-new-dark-fire-deodorants-combo/p/itmeyuxvakeuzsty?pid=CAGEYUXVAKNKDUUV",
          "http://www.flipkart.com/adidas-deo-combo-set/p/itmduycczrgcgcs3?pid=CAGDUYCCZRGCGCS3",
          "http://www.flipkart.com/tp-link-tl-wr841n-300mbps-wireless-n-router/p/itmd7hn9cw5y3h3k?pid=RTRD7HN3JJYF6WN2",
          "http://www.flipkart.com/axe-deodorant-combo-set/p/itme6symn2trwdgt?pid=CAGE6SYMVUA8FPT8",
          "http://www.flipkart.com/tenda-fh330/p/itme7dbhgdedvr3v?pid=RTRE7DBH3ZDKADUS",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdtax23hbqb8zy?pid=NKCDTAXF4CZFDXGZ",
          "http://www.flipkart.com/d-link-dir-605l-wireless-n300-cloud-router/p/itmdtp8dugtb5jdy?pid=RTRDBECHFKZTHEP8",
          "http://www.flipkart.com/edimax-br-6228ns-v2/p/itmdzbj58nvhcdgh?pid=RTRDZBJ5GRMDUZ8H",
          "http://www.flipkart.com/engage-spell-mate-combo-set/p/itmdvvyfucsgxjdm?pid=CAGDVVX9HE6C9WYF",
          "http://www.flipkart.com/avon-little-black-white-dress-body-each-150-ml-combo-set/p/itme3gfttyvk2zwp?pid=CAGE3GFTPMNXPZAG",
          "http://www.flipkart.com/yardley-red-roses-combo-set/p/itme6fykndhcgzs6?pid=CAGE6FYKYKQEWRBS",
          "http://www.flipkart.com/klassik-animal-random-art-card-board-pencil-box/p/itme7ny9szpqgqnz?pid=PBXE7NY9ZRYZFBAZ",
          "http://www.flipkart.com/tp-link-archer-c20-ac750-dual-band-router/p/itme8gkfgb5hyqzq?pid=RTRE8GKF2CUJ2GNN",
          "http://www.flipkart.com/alex-s-super-fine-series-ben-ten-art-metal-pencil-box/p/itmebyhckvrvt3pf?pid=PBXEBFGFRM5797BZ",
          "http://www.flipkart.com/klassik-3d-big-eyes-random-art-cloth-pencil-box/p/itme8bte6rmesdu2?pid=PBXE8BTEMTBZXPKE",
          "http://www.flipkart.com/netgear-n300-wireless-adsl2-modem-router-mobile-broadband-dgn2200m/p/itmd6ffbdr5ugd8z?pid=RTRD6FYYWFHEYJYE",
          "http://www.flipkart.com/netgear-wndr4000-n750-wireless-dual-band-gigabit-router/p/itmd4d3ffheg6hft?pid=RTRD4D3EGBAYBG2C",
          "http://www.flipkart.com/kamasutra-combo-set/p/itme22efgdcyfzff?pid=CAGE22EFFAPMZEPE",
          "http://www.flipkart.com/fabseasons-fashion-fruit-art-faux-fur-pencil-boxes/p/itme9ejknwgj82gn?pid=PBXE9EJKVEFQQTJH",
          "http://www.flipkart.com/tenda-3g300m/p/itmdngvvaktbzf6c?pid=RTRDNGVMRQ63YU54",
          "http://www.flipkart.com/giftwallas-crystal-necklace/p/itmefkbytsc2qyhk?pid=NKCEFKBYDZMHUYZK",
          "http://www.flipkart.com/huawei-ws322-300-mbps-mini-wireless-router-cum-repeater/p/itmefwynhhequyzg?pid=RTREFWYNCYFURU5G",
          "http://www.flipkart.com/smc-wbr14s/p/itmdruzcbfab9hbk?pid=RTRDRUZCPNJ3MTAT",
          "http://www.flipkart.com/anna-andre-paris-floralina-red-horizon-combo-set/p/itmdtn27rakr3z36?pid=CAGDTN27DEWJYUHK",
          "http://www.flipkart.com/netgear-jwnr2010-n300-wireless-router/p/itmdpxkcezfz7rhd?pid=RTRDPXKCBHEECZQE",
          "http://www.flipkart.com/informatix-acrylic-necklace/p/itme5u69zr39fzmq?pid=NKCE5U69HB8JAUTU",
          "http://www.flipkart.com/belkin-dual-band-wireless-range-extender/p/itmdetbdbnyfdudu?pid=RTRDETBCPG9XNHUY",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdtax2rjadxtzy?pid=NKCDTAXFXWPKGZAN",
          "http://www.flipkart.com/neo-gold-leaf-fancy-school-art-cloth-pencil-box/p/itmeat5yqxfxkpbd?pid=PBXEAT5YEBXXHPEW",
          "http://www.flipkart.com/huawei-hg532d-adsl2-300-mbps-modem-router/p/itme978xrhkmfbsa?pid=RTRE978WCZ6B8GPW",
          "http://www.flipkart.com/tara-lifestyle-dora-printed-art-plastic-pencil-box/p/itme9rams6sx7ree?pid=PBXE9RAMEEYHARYC",
          "http://www.flipkart.com/french-factor-combo-set/p/itme2mac5np8ntxd?pid=CAGE2MACSYZCWHFG",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdsxagwjejyxyu?pid=NKCDSXA5G2KQYSAS",
          "http://www.flipkart.com/netgear-ac2350-nighthawk-x4-smart-wifi-router-r7500/p/itmefr78phq3zgzw?pid=RTREFR77EH5G8AH4",
          "http://www.flipkart.com/vodafone-r206-i/p/itmeayagepka6rsv?pid=RTREAYAG9RFZPYNP",
          "http://www.flipkart.com/aeoss-300mbps-wireless-n-multifunction-mini-router-repeater-lan-ports-wall-powered/p/itme3f95gndg3ye8?pid=RTRE3F95FDUDKB8Z",
          "http://www.flipkart.com/tp-link-n600-wireless-dual-band/p/itmdpfnayqzqmcg3?pid=RTRDPFNAFVJAXHTA",
          "http://www.flipkart.com/netis-wf2419-n300-wireless-router/p/itmdmtetzzffp6mv?pid=RTRDMTEPFH3EVUM6",
          "http://www.flipkart.com/etti-esj86-multi-glass-necklace/p/itme96sxbwrpd9ra?pid=NKCE96SXZUY5TZPS",
          "http://www.flipkart.com/cubetek-airmobi-iplay2-wifi-music-router/p/itme2pjpxuj67mjq?pid=RTRE2PJPQTZHAH4H",
          "http://www.flipkart.com/adidas-ice-dive-combo-set/p/itme46yzbeejzwgr?pid=CAGE46YZPYX7BVUK",
          "http://www.flipkart.com/outshiny-eagle-printed-art-polyester-pencil-box/p/itme4rb3qywe3nfw?pid=PBXE4RB3Y3GXWPFV",
          "http://www.flipkart.com/axe-apollo-combo-set/p/itmdy6ggg6hyafbj?pid=CAGDY6GGGVXY9ZGS",
          "http://www.flipkart.com/belkin-basic-surf-n300-router/p/itmdffysphy699cy?pid=RTRDFFYGKJAXPUUG",
          "http://www.flipkart.com/nike-combo-set/p/itme44j5gt9cvmsz?pid=CAGE44J5UXNHXFYH",
          "http://www.flipkart.com/asus-ea-n66-dual-band-wireless-n900-gigabit-3-in-1-ap-wi-fi-bridge-ra/p/itmdzzb62w7zchnb?pid=RTRDZ7CGNGRHHRCM",
          "http://www.flipkart.com/legrand-myrius-673031-25a-motor-starter-white-25-one-way-electrical-switch/p/itme4ystxz8hyxad?pid=SCHE4YST3GFY8AYU",
          "http://www.flipkart.com/cinthol-rush-dive-play-combo-set/p/itme7nv6gzfkskhf?pid=CAGE7NV6JUTZVFXV",
          "http://www.flipkart.com/anna-andre-paris-red-horizon-deodorant-combo-set/p/itme22ee7hnephbf?pid=CAGE22EEX2HKGXFQ",
          "http://www.flipkart.com/pinnakle-dual-compartment-utility-pouch-v2-solid-art-polyester-pencil-box/p/itme4qfhp9erhcnx?pid=PBXE4QFH2BXJGRMG",
          "http://www.flipkart.com/netgear-ac-750-wi-fi-range-extender/p/itmdykuhykgaz6n8?pid=RTRDYKU6F2GVR3CR",
          "http://www.flipkart.com/avon-little-black-dress-body-each-150-ml-combo-set/p/itme3gftwgu5eatv?pid=CAGE3GFTQ3UHZ4TC",
          "http://www.flipkart.com/npplastics-52mm-0-45x-dslr-wide-angle-macro-nikon-canon-mechanical-lens-adapter/p/itme8ukzpwfcxgzs?pid=LEAE8UKZFQRUTMAG",
          "http://www.flipkart.com/iball-wr7011a/p/itmdw77ygagzpxpt?pid=RTRDW77Y4D3QTBUG",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdu9c3zbmu4cgr?pid=CAGDU9C3ZBMU4CGR",
          "http://www.flipkart.com/tenda-n6/p/itmdngvvn4gyucat?pid=RTRDNGVMAKRQKH7Y",
          "http://www.flipkart.com/zeva-keepz-u-gift-set-combo/p/itmdypbwwbeesrr2?pid=CAGDYPBWA7RBUBYT",
          "http://www.flipkart.com/d-link-dap-1320-wireless-range-extender/p/itmdqz8pegbfthqs?pid=RTRDQZ8Z72FRMKGX",
          "http://www.flipkart.com/iball-wra300n3gt/p/itmecrf7gv7fcw45?pid=RTRECRF7ND5CVZZX",
          "http://www.flipkart.com/apple-me918hn-a/p/itmdnhmsakxhmhjq?pid=RTRDNHMRFZTR3ZPZ",
          "http://www.flipkart.com/tenda-te-d151-n150-wireless-adsl2-modem-router/p/itmdzk8xden3grcy?pid=RTRDZK8XRESZY5YT",
          "http://www.flipkart.com/wi-bridge-apw40-01/p/itmefdxtsfsjn4de?pid=RTREFDXTYEHF94PJ",
          "http://www.flipkart.com/outshiny-dual-compartment-printed-art-polyester-pencil-box/p/itme4rb4uwqnzhhj?pid=PBXE4RB4BZYTMFGY",
          "http://www.flipkart.com/netgear-wn2000rpt-universal-wifi-range-extender/p/itmd6ffbh2rbacyj?pid=RTRD6FYY9KH3BBGZ",
          "http://www.flipkart.com/french-factor-man-year-deodorant-gift-set-combo/p/itme4gf7gzhmzhjz?pid=CAGE4GF7UWGZHN7J",
          "http://www.flipkart.com/tenda-w268r/p/itmdngvvfzmdvgu6?pid=RTRDNGVMW9BGYHPH",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdudg8fhxxuyjs?pid=CAGDUDG8FHXXUYJS",
          "http://www.flipkart.com/outshiny-dual-compartment-printed-art-polyester-pencil-box/p/itme4rb4rtmmpphd?pid=PBXE4RB3HNFDXGGN",
          "http://www.flipkart.com/asus-rt-n16-multi-functional-gigabit-wireless-n-storage-printer-media-server-router/p/itmd3849gchg9wp2?pid=RTRD3849TERR75YB",
          "http://www.flipkart.com/tenda-w150d/p/itmdp2cxr8frpjbf?pid=RTRDNY65ZSSBBXCZ",
          "http://www.flipkart.com/asus-rt-n15u-wireless-n300-gigabit-router/p/itmda5pju6zanzmm?pid=RTRDA4U7RSHNZEGW",
          "http://www.flipkart.com/adidas-champions-league-dynamic-pulse-combo-set/p/itme6hyjhvmpxpgh?pid=CAGE6HYJDNZJVADS",
          "http://www.flipkart.com/toto-link-f1-150-mbps-wireless-n-soho-fiber-router/p/itmdyyvfgugnzqca?pid=RTRDYYTZSUUNFFUT",
          "http://www.flipkart.com/playboy-new-york-combo-set/p/itmebkz2sm6cfpdg?pid=CAGE5HYNQNGHJ2TY",
          "http://www.flipkart.com/nike-n5th-element-combo-set/p/itme8scpv2fhhygh?pid=CAGE8SCPTWXNZWC6",
          "http://www.flipkart.com/izotron-wr40003g-3g-pocket-router/p/itmdrjf8uybafezx?pid=RTRDRJF8GJ5AFZTG",
          "http://www.flipkart.com/tp-link-4-port-cable-dsl-tl-r460/p/itmdpa9hgcfdvacp?pid=RTRDPA9FNCRGS8UZ",
          "http://www.flipkart.com/belkin-play-max-router/p/itmdffysbcyexmjc?pid=RTRDFFYGSSX2BYWU",
          "http://www.flipkart.com/dress-villa-acrylic-alloy-necklace/p/itmdyga8wyrbtug5?pid=NKCDYGA7HK76EBFC",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdsrpbczeeuazx?pid=NKCDSRPA8HZF94S4",
          "http://www.flipkart.com/tp-link-tl-wdr4300-n750-wireless-dual-band-gigabit-router/p/itmdhcxzbhyszzhz?pid=RTRDHCXZPWGDJRVH",
          "http://www.flipkart.com/park-avenue-good-morning-combo-set/p/itmdwgcydeahhpmu?pid=CAGDWGCSQTYKCUG7",
          "http://www.flipkart.com/binatone-wr1500n/p/itme2tynztgwkhvx?pid=RTRE2TYNWTGTPE8D",
          "http://www.flipkart.com/klassik-girly-random-art-cloth-pencil-box/p/itme82kpgh9eun6g?pid=PBXE82KPEFNGC5CH",
          "http://www.flipkart.com/d-link-dir-505-all-in-one-mobile-companion-router/p/itmdekmqrj4czdj4?pid=RTRDEHFF6AJRARJ3",
          "http://www.flipkart.com/indian-charm-glass-metal-necklace/p/itme8rb52nnryneq?pid=NKCE8RB5WMWAWNHJ",
          "http://www.flipkart.com/jewellerywale-alloy-necklace/p/itmeabathzad3ryt?pid=NKCEABATK2R74GPJ",
          "http://www.flipkart.com/zyxel-vmg1312-b10a-vdsl2-wireless-n-4-port-gateway-usb/p/itmdwgaknhghzbyp?pid=RTRDWGAKVZK8VQ9R",
          "http://www.flipkart.com/netgear-d3600-n600-dual-band-gigabit-wi-fi-modem-router/p/itme8gjt2phbhgts?pid=RTRE8GJTHFTTDZWA",
          "http://www.flipkart.com/d-link-dsl-2520u/p/itmd2a539czjjnrh?pid=RTRE2XBZFFEZRCFZ",
          "http://www.flipkart.com/kamasutra-combo-set/p/itme2xc2rxbytndd?pid=CAGE2XC2CTC2TWRJ",
          "http://www.flipkart.com/dressvilla-beads-alloy-necklace/p/itmdyg8bcxvzrhgg?pid=NKCDYG8BDVKZ7GP8",
          "http://www.flipkart.com/tp-link-300-mbps-universal-wifi/p/itmdp2gvgwfkffb2?pid=RTRDP2GSBX4AF7FK",
          "http://www.flipkart.com/anna-andre-paris-dark-red-horizon-majesty-combo-set/p/itmdtn27ajk2zgng?pid=CAGDTN27KGFHHVHJ",
          "http://www.flipkart.com/tp-link-td-w8970/p/itmdxv6bywqjjbw2?pid=RTRDXV6BA5PZAEPH",
          "http://www.flipkart.com/yardley-english-rose-festive-collection-pack-combo-set/p/itme3mweqkvqvrpz?pid=CAGE3MWEW2FZFB9P",
          "http://www.flipkart.com/united-colors-benetton-sport-combo-set/p/itmea3jmzt3vaze5?pid=CAGEA3JMBZUV5DQV",
          "http://www.flipkart.com/denim-deo-combo-set/p/itmdtfstyfyqzurj?pid=CAGDTFSHTF6TRBFZ",
          "http://www.flipkart.com/tp-link-td-w8151n-150mbps-wireless-n-adsl2-modem-router/p/itmdrrazxrqkdzyn?pid=RTRD7HN3BBE7G9YT",
          "http://www.flipkart.com/cinthol-deo-spray-intense-pack-2-combo-set/p/itmdw63hefeduy9j?pid=CAGDW63HG5JBCVGA",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4ksyyped6?pid=NKCE4VA4EDK86BCN",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdu85yywzhhngt?pid=CAGDU85YYWZHHNGT",
          "http://www.flipkart.com/beverly-hills-polo-club-combo-set/p/itmdrjj4vt2arj4u?pid=CAGDRJJ3HUNXZPND",
          "http://www.flipkart.com/hi-look-alloy-necklace/p/itmdw898n7vyrq88?pid=NKCDW898GSGZQGGY",
          "http://www.flipkart.com/linksys-ea6700-dual-band-n450-ac1300-hd-video-pro/p/itmdpeuppvzgq8zz?pid=RTRDPEUPQRZGWHGC",
          "http://www.flipkart.com/axe-deodorant-combo-1-offer-set/p/itme6symdvqvyqg8?pid=CAGE6SYMP5TEQVMT",
          "http://www.flipkart.com/netgear-d1500/p/itmef3pr4q4qhccb?pid=RTREF3PRF3M9FMEF",
          "http://www.flipkart.com/d-link-dir-803/p/itmey9xyycdkyzxg?pid=RTREY9XYN7YUJTFR",
          "http://www.flipkart.com/tp-link-tl-wa830re-300-mbps-wireless-n-range-extender/p/itmdmnvgqz7anyx4?pid=RTRDMNVF7CQ3HAHU",
          "http://www.flipkart.com/jdx-alloy-necklace/p/itme4va4ubygchwg?pid=NKCE4VA4WZWGGXUT",
          "http://www.flipkart.com/tp-link-archer-c2-ac750-wireless-dual-band-gigabit-router/p/itme387pzehzzdmy?pid=RTRE387ZG6JUHDHP",
          "http://www.flipkart.com/d-link-dir-600-n150-wireless-router/p/itmdpeg8x3y5zxkn?pid=RTRDPEG7ATGCPYZS",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdu9c36ebypdrp?pid=CAGDU9C36EBYPDRP",
          "http://www.flipkart.com/d-link-dir-510l/p/itmebwvareshnbns?pid=RTREBWVASMXDVRNG",
          "http://www.flipkart.com/trendnet-n300-wireless-home-router/p/itmdqzz3evzjk8w6?pid=RTRDQZMJYG3JQ7PM",
          "http://www.flipkart.com/asus-dsl-n12u-wireless-n300-adsl-modem/p/itmdhy5kshwwr2bn?pid=RTRDHYYVXHYG93NF",
          "http://www.flipkart.com/my-ego-combo-set/p/itmdu9c3qvcbmqkq?pid=CAGDU9C3QVCBMQKQ",
          "http://www.flipkart.com/d-link-dir-600l/p/itmdbemyeh7t8rkt?pid=RTRE9JEGMXHZ5RHQ",
          "http://www.flipkart.com/nuroma-men-s-fashion-black-label-combo-set/p/itme8fg3egfxm3gt?pid=CAGE8FG3CYVFG2GM",
          "http://www.flipkart.com/spinz-combo-set/p/itme3fx77hfsyzq5?pid=CAGE3FX7XZGYHGRJ",
          "http://www.flipkart.com/digisol-300-mbps-wireless-adsl2-broadband-router/p/itmd8fserg7czagy?pid=RTRD8FPJEQRZ6BEM",
          "http://www.flipkart.com/nba-knicks-chicago-bull-miami-heat-combo-set/p/itmdsgyt2tbcenzr?pid=CAGDSGY5KU3VWEAY",
          "http://www.flipkart.com/pinnakle-dual-compartment-utility-pouch-v4-printed-art-resin-pencil-box/p/itme7yyyszgzngbg?pid=PBXE7YYYF4Y48TYX",
          "http://www.flipkart.com/netgear-mbrn3000-3g-mobile-broadband-wireless-n-router/p/itmd6ffbwgzuhffm?pid=RTRD6FYYUQZJBY6F",
          "http://www.flipkart.com/asus-dsl-n55u-wireless-n600-gigabit-router/p/itmda5pjznegqzzu?pid=RTRDA4U7UE3Z7UMB",
          "http://www.flipkart.com/smartcraft-generic-netted-art-cloth-pencil-box/p/itme4q7yfdqxyhng?pid=PBXE4Q7YW6GNMRTE",
          "http://www.flipkart.com/tp-link-tl-wdr3600-n600-wireless-dual-band-gigabit-router/p/itmdmnvgjbhjzcye?pid=RTRDMNVFYZZBXT3G",
          "http://www.flipkart.com/asus-rp-n53-dual-band-wireless-n600-range-extender/p/itmdq4hqzfcws3sx?pid=RTRDQ4HQC6A4ZC4G",
          "http://www.flipkart.com/engage-combo-set/p/itmdunh3dynz4zhn?pid=CAGDUNH36EAX85G8",
          "http://www.flipkart.com/tenda-te-d-303-n300-adsl2-modem-router-usb-port/p/itmdzk8xxzwutejg?pid=RTRDZK8XCUEKZDFZ",
          "http://www.flipkart.com/skc-steering-cover/p/itme2v2afvbadtjh?pid=CSOE2V29ZTH5A3QU",
          "http://www.flipkart.com/digisol-150-mbps-wireless-green-broadband-router/p/itmd8fsejbpyjayx?pid=RTRD8FPJQUFYZAPJ",
          "http://www.flipkart.com/eva-combo-set/p/itme2ncrpjw6gdn2?pid=CAGE2NCRSPGZ5XN5",
          "http://www.flipkart.com/jewels-guru-alloy-necklace/p/itmecffwhsvkdgex?pid=NKCECFFWZVMTHUYK",
          "http://www.flipkart.com/tp-link-td-w8968-300-mbps-wireless-n-usb-adsl2-modem-router/p/itmdggsyph7ytbfx?pid=RTRDGGQ754BDWH7U",
          "http://www.flipkart.com/digisol-dg-bg4100n/p/itmdvfaphcq8dzpy?pid=RTRDVFAPZMNA8CHC",
          "http://www.flipkart.com/french-factor-combo-set/p/itme2machbev9qpq?pid=CAGE2MACSFZRQEEV",
          "http://www.flipkart.com/playboy-london-new-york-combo-set/p/itme4bqxe3nrh7c2?pid=CAGE4BQXSBKGWBE3",
          "http://www.flipkart.com/playboy-berlin-combo-set/p/itmebkz3utygvkkb?pid=CAGE5HYNWQYHCGQS",
          "http://www.flipkart.com/wi-bridge-wr3g050-01/p/itmefdxtd9ndxgf5?pid=RTREFDXTZ4GGGAEX",
          "http://www.flipkart.com/beetel-adsl2-router-450tc3-pci-internal-modem/p/itmdzzphmjgryrs4?pid=ILMDZZPH32VEPGBZ",
          "http://www.flipkart.com/neo-gold-leaf-travel-fancy-art-plastic-pencil-box/p/itme78phamdmg4bb?pid=PBXE78PHMWRZDD94",
          "http://www.flipkart.com/belkin-n300-adsl2-wireless-router-modem/p/itmdg5cr7hgepfvw?pid=RTRDG5C6V3YVWSH6",
          "http://www.flipkart.com/nike-orange-combo-set/p/itme8x8xr9nytggz?pid=CAGE8X8XGZGQGWVN",
          "http://www.flipkart.com/armaf-vanity-femme-pink-combo-set/p/itme9agrxfxa99pw?pid=CAGE9AGRG58XZWVT",
          "http://www.flipkart.com/asus-dsl-n12e-300-mbps-wireless-adsl-modem-router/p/itmefh84bwdhdemz?pid=RTREFH7UWNEQDHAY",
          "http://www.flipkart.com/netgear-n600-wireless-dual-band-gigabit-adsl2-modem-router-dgnd3700/p/itmd6ffbdjgc8xgj?pid=RTRD6FYY7B26SHXC",
          "http://www.flipkart.com/tenda-3g622r/p/itmdp2cmryfrjhkc?pid=RTRDNGVMCGNCTWUU",
          "http://www.flipkart.com/nike-combo-set/p/itme2zhbkyzpmzft?pid=CAGE2ZHBSKWHSHKH",
          "http://www.flipkart.com/jdx-brass-necklace/p/itme4va4pnhj6ytd?pid=NKCE4VA4FAZ7FTFM",
          "http://www.flipkart.com/d-link-dsl-2750u-wireless-n-300-adsl2-4-port-wi-fi/p/itmd4ky52tgtbawn?pid=RTRD4KY4UNGYCZFG",
          "http://www.flipkart.com/adidas-combo-set/p/itme22ee4ghersh7?pid=CAGE22EE8ZG8HCS6",
          "http://www.flipkart.com/netgear-wn3000rp-universal-wi-fi-range-extender/p/itmd6ffb7xwg49mv?pid=RTRD6FYYZCZGPCVH",
          "http://www.flipkart.com/adidas-floral-dream-combo-set/p/itme6gqcbdf2czet?pid=CAGE6GQCCDSWABFT",
          "http://www.flipkart.com/zingalalaa-lp-50-50-lm-led-corded-portable-projector/p/itmeajtt5qeteamm?pid=PPJEAJTT86WKA5G9",
          "http://www.flipkart.com/totalcare-expert-metal-glass-shiner-car-washer/p/itmeg69tbjzmhsub?pid=CWLEG69T7RRKTZNR",
          "http://www.flipkart.com/indiano-flip-flops/p/itmegw39wpnhx6ej?pid=SFFEGW39MZHHGBEF",
          "http://www.flipkart.com/blacksmith-analog-wall-clock/p/itme2tfyzazksmf4?pid=WCKE2TFYRTHGTUTC",
          "http://www.flipkart.com/prestige-popular-plus-10-l-pressure-cooker/p/itmdyz98q7cxyzye?pid=PRCDYWYKEKFFDGBP",
          "http://www.flipkart.com/prestige-deluxe-plus-10-l-pressure-cooker/p/itmdyaqzhbqrrpjb?pid=PRCDXZP2ZFHQHUH7",
          "http://www.flipkart.com/fcs-suzuki-metal-key-chain/p/itme24gedavajkbq?pid=CBRE24GEGUHRSZAQ",
          "http://www.flipkart.com/milton-school-750-ml-water-bottle/p/itmdmeztreach7hh?pid=WBTDMEZTDSZGZEDJ",
          "http://www.flipkart.com/milton-school-1000-ml-water-bottle/p/itmdmeztwxnkarne?pid=WBTDMEZTUWBPD5DM",
          "http://www.flipkart.com/elligator-women-sports-sandals/p/itmebg86hngjhvsd?pid=SNDEBG864TPNPGSE",
          "http://www.flipkart.com/revine-men-s-printed-casual-shirt/p/itmeaggfazcpmr3y?pid=SHTEAGGFBZGZMFCF",
          "http://www.flipkart.com/tracer-women-sports-sandals/p/itme3snf9gcjjfe2?pid=SNDE3SNFMHARS463",
          "http://www.flipkart.com/wrogn-men-s-solid-casual-shirt/p/itmeb9bvdfjzaudn?pid=SHTEB9BVH2S3XYCY",
          "http://www.flipkart.com/prestige-nakshatra-alpha-7-l-pressure-cooker/p/itmefr82qpsptcsf?pid=PRCEFR7WX4AFUXZN",
          "http://www.flipkart.com/maharaja-whiteline-neo-mx-147-500-w-mixer-grinder/p/itmeamvtqd6qjyag?pid=MIXEAMVTVJAGVMCF",
          "http://www.flipkart.com/nba-women-s-solid-ankle-length-socks/p/itme7732ath5qatd?pid=SOCE7732ARDEF7UF",
          "http://www.flipkart.com/stiga-orion-table-tennis-racquet/p/itmdt69teny9gxce?pid=RAQDCNWAGART9UVZ",
          "http://www.flipkart.com/gki-euro-star-table-tennis-racquet/p/itmdehgyrdg5quvg?pid=RAQDEHGUB5VZTC8H",
          "http://www.flipkart.com/stag-4-star-table-tennis-racquet/p/itmdt69tyddxxcng?pid=RAQDCNWAHJK9JNUY",
          "http://www.flipkart.com/blacksmith-analog-wall-clock/p/itme2tffgm9c7zsp?pid=WCKE2TFF4ZYGXUMH",
          "http://www.flipkart.com/dhhan-8-watt-rechargeable-emergency-lights/p/itmegmzryqghhayf?pid=EMLEGMZRZGDARGR8",
          "http://www.flipkart.com/jbn-creation-girl-s-kurti-legging-dupatta-set/p/itmegjbakg2ad4yg?pid=ETHEGJBAZPGQBURA",
          "http://www.flipkart.com/cayman-solid-boy-s-track-suit/p/itmeeb9muyzq7sxn?pid=TKSEEB9MNUGDS9DZ",
          "http://www.flipkart.com/blessed-ring-basket-plant-container-set/p/itmdy5axbnfhvqrd?pid=PCSDY5AHFNSPGSV8",
          "http://www.flipkart.com/rk-plant-container-set/p/itme2zfd2gggnavs?pid=PCSE2ZFDBB3N4PTP",
          "http://www.flipkart.com/vgreen-plant-container-set/p/itme9q6v9wyh8vha?pid=PCSE9Q6VCVMWRAPN",
          "http://www.flipkart.com/rk-plant-container-set/p/itme2zfd8fhmfzcw?pid=PCSE2ZFDJJGFNHC7",
          "http://www.flipkart.com/adorn-women-wedges/p/itmedkkwpsttkgea?pid=SNDEDKKWEAFRMDR9",
          "http://www.flipkart.com/blessed-gamla-basket-plant-container-set/p/itmdy5ax8bhyu4dm?pid=PCSDY5AHHQSXZARH",
          "http://www.flipkart.com/cenizas-casual-printed-women-s-kurti/p/itme39q4g2wmyzjd?pid=KRTE39Q4GVHFHWZV",
          "http://www.flipkart.com/martha-plant-container-set/p/itmea7hbgxy8dvkr?pid=PCSEA7HBHMUNHZRP",
          "http://www.flipkart.com/do-bhai-women-wedges/p/itmdxfqhh8r3kvfy?pid=SNDDXFQHUDJDHZG2",
          "http://www.flipkart.com/natures-plus-img-0004-plant-container-set/p/itmectytn52wg7xj?pid=PCSECTYTDV7DGJ4R",
          "http://www.flipkart.com/blessed-jaali-basket-plant-container-set/p/itmdy5axzzzswetk?pid=PCSDY5AFPGSUPEUF",
          "http://www.flipkart.com/easy-gardening-8-inch-plant-container-set/p/itme95hxpbeasvua?pid=PCSE95HXQE744G8Z",
          "http://www.flipkart.com/easy-gardening-10-inch-square-plant-container-set/p/itme93h4k4bmuukf?pid=PCSE93H4FSGSJHU6",
          "http://www.flipkart.com/yellow-door-planters-tray-tea-light-holders-green-plant-container-set/p/itme2djz2hs53hvb?pid=PCSE2DJZ4RMMXBUG",
          "http://www.flipkart.com/dgb-hp-500-520-hstnn-ib44-6-cell-laptop-battery/p/itmdsuzkeegqgheu?pid=ACCDSUZJGMZD9FHZ",
          "http://www.flipkart.com/rk-plant-container-set/p/itme2zfd4fpw8zkm?pid=PCSE2ZFDEWEJFKPY",
          "http://www.flipkart.com/go-hooked-mini-table-plant-container-set/p/itmdyqfgwwwdgfhf?pid=PCSDYQEVGFZSGRQJ",
          "http://www.flipkart.com/sutra-decor-handmade-metallic-petals-planters-plant-container-set/p/itme5ngbk4rwvgyk?pid=PCSE5N9BAHDXCSVB",
          "http://www.flipkart.com/remson-india-brown-medium-women-wedges/p/itme3fpzeqggfvgm?pid=SNDE3FPZ3A4JCXRH",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5ax9hrpg9us?pid=PCSDY5AFHRHDHPZR",
          "http://www.flipkart.com/blessed-plain-plant-container-set/p/itmdy5axzynknnj8?pid=PCSDY5AHERHZSZZW",
          "http://www.flipkart.com/ten-suade-black-women-wedges/p/itmdzpvyyur9nks9?pid=SNDDZPVYKFSZJF35",
          "http://www.flipkart.com/ten-suade-red-women-wedges/p/itmdzpvyrnk8qkge?pid=SNDDZPVZ3HZTC7DB",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5axk3y4xgyd?pid=PCSDY5AFBNKGE3AY",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5bfj7rhgpke?pid=PCSDY5AFMETYABEH",
          "http://www.flipkart.com/first-smart-deal-plant-container-set/p/itmeayrt3gawhfrh?pid=PCSEAYRTZYDSPGMB",
          "http://www.flipkart.com/easy-gardening-12-inch-square-plant-container-set/p/itme93h3hqghpewc?pid=PCSE93H3KFSDC6ZY",
          "http://www.flipkart.com/easy-gardening-10-inch-nursery-plant-container-set/p/itmeah5wmvw3hrxz?pid=PCSEAH5WVHDU2YF8",
          "http://www.flipkart.com/lapguard-lenovo-ideapad-v470-6-cell-laptop-battery/p/itmdvpgknnfqar4k?pid=ACCDVPGKY3GBDB5P",
          "http://www.flipkart.com/clublaptop-sony-vgn-bps22-bps22a-6-cell-laptop-battery/p/itmdpdjzfgfnuqft?pid=ACCDPDJVGNGNX7QE",
          "http://www.flipkart.com/beverly-hills-polo-club-solid-women-s-tunic/p/itme5y759n4szuhf?pid=TUNE5Y75EKJKWVRM",
          "http://www.flipkart.com/dolphin-miles-women-wedges/p/itme7dzg26przcnf?pid=SNDE7DZGGD2JVRBN",
          "http://www.flipkart.com/dolphin-miles-women-wedges/p/itme85chq4z4qrvz?pid=SNDE85CH2PN36BUZ",
          "http://www.flipkart.com/dolphin-miles-women-wedges/p/itme9grptjys4xrh?pid=SNDE9GRQJQQ76ESA",
          "http://www.flipkart.com/go-hooked-basket-plant-container-set/p/itmdyqfz6hapmyct?pid=PCSDYQEWUYFPRUWY",
          "http://www.flipkart.com/dolphin-miles-women-wedges/p/itme9gypxpbwp2vt?pid=SNDE9GYPHPHJZXB7",
          "http://www.flipkart.com/green-girgit-plant-container-set/p/itmeakvbj8mpvgnh?pid=PCSEAKVBS6ZDETVX",
          "http://www.flipkart.com/hako-hp-compaq-presario-cq45-106au-6-cell-laptop-battery/p/itmdydy6zhnadhfh?pid=ACCDYDY6DPCHAN7Y",
          "http://www.flipkart.com/go-hooked-mini-table-plant-container-set/p/itmdyqfgw2eycrgz?pid=PCSDYQEV8G2ZGBNM",
          "http://www.flipkart.com/natures-plus-home-garden-plant-container-set/p/itme4fkcxwzbtt6j?pid=PCSE4FKCZ23EPQFS",
          "http://www.flipkart.com/arb-hp-compaq-presario-cq45-compatible-black-6-cell-laptop-battery/p/itmdy6gththvtxc9?pid=ACCDY6GTHNEAPHM3",
          "http://www.flipkart.com/hp-compaq-presario-cq43-6-cell-laptop-battery/p/itmdsy8emjhndp4y?pid=ACCDSY8EHJF6GRMG",
          "http://www.flipkart.com/hako-hp-compaq-presario-cq45-207tu-6-cell-laptop-battery/p/itmdydy6xutpfjwk?pid=ACCDYDY68JNBV4BZ",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5axbysksehd?pid=PCSDY5AFGFAQNCY9",
          "http://www.flipkart.com/green-girgit-plant-container-set/p/itmeakvbtpmpezrv?pid=PCSEAKVBGC7CJQZT",
          "http://www.flipkart.com/fastrack-nd9912pp11j-teevirus-analog-watch-men-women/p/itmdkb7zzzz8efx7?pid=WATDKB7JA52JZRRU",
          "http://www.flipkart.com/sonata-8015yl01-analog-watch-women/p/itmdg9fyvhwq6g7n?pid=WATDG9F74GYWEH4U",
          "http://www.flipkart.com/sonata-8959yl02-yuva-gold-analog-watch-women/p/itmda5wag4b4xek3?pid=WATDA5ZA5FQVGMHA",
          "http://www.flipkart.com/flippd-fdlsp1507-analog-watch-women/p/itme3hwhmdhg6fc4?pid=WATE3HFNMGVTZEDS",
          "http://www.flipkart.com/do-bhai-400-women-wedges/p/itme6akuyzchxwkb?pid=SNDE6AKUC72HPWZF",
          "http://www.flipkart.com/geonaute-1620362-digital-watch-men/p/itmdp2zfsa7b4x49?pid=WATDNJVHHKXKVRGF",
          "http://www.flipkart.com/maxima-21104bmly-gold-analog-watch-women/p/itmdsv3uqagpbrhz?pid=WATDSV3UUCTKQ4ZD",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5axrnh5tqza?pid=PCSDY5AFZYUTHYZX",
          "http://www.flipkart.com/sonata-7086sl04-tech-1-analog-watch-men/p/itmda5watzjcpcu8?pid=WATDA5ZANJ7UZ74Q",
          "http://www.flipkart.com/maxima-25061cmly-gold-analog-watch-women/p/itmdsv448zzxzyhp?pid=WATDSV3UMUNAXURA",
          "http://www.flipkart.com/sonata-everyday-analog-watch-men/p/itmdffj7yr3yryvf?pid=WATDFFH3PGFHHZH8",
          "http://www.flipkart.com/figo-fashion-ll-1006blk-analog-watch-women/p/itmdsw8py5f3xezc?pid=WATDSW7X8FTCNSHQ",
          "http://www.flipkart.com/maxima-07011lcgc-attivo-analog-watch-men/p/itme26j8zy7zyn5h?pid=WATE26J7MSP5GPSY",
          "http://www.flipkart.com/color-palatte-plant-container-set/p/itme5wb8vzhjku6a?pid=PCSE5WB883R4ZNUN",
          "http://www.flipkart.com/fastrack-9913pp05-tees-analog-watch-men/p/itmd9gjfz7dzkqax?pid=WATD9H76GH2CHZ48",
          "http://www.flipkart.com/nexus-nx-7587-analog-watch-women/p/itmdxfgtnuqzzzzx?pid=WATDXFGTUVJZYXRD",
          "http://www.flipkart.com/maxima-03918cmly-analog-watch-women/p/itme26j8myzhdhrz?pid=WATE26J7Z9MEZZKH",
          "http://www.flipkart.com/sonata-8959yl01-yuva-gold-analog-watch-women/p/itmda5wawcyk9pby?pid=WATDA5ZAGNMGD5EJ",
          "http://www.flipkart.com/hmt-b0341-hq-analog-watch-women/p/itmdqg96aybyzr7g?pid=WATDHHAS7U8XAFZJ",
          "http://www.flipkart.com/maxima-24990lmli-swarovski-analog-watch-women/p/itmdcuj4hfn97rj6?pid=WATDCUGXHXSUHBHX",
          "http://www.flipkart.com/sonata-2160yl06-economy-analog-watch-women/p/itmdg9fy7hafuvvu?pid=WATDG9F7TQKGHZHQ",
          "http://www.flipkart.com/maxima-32841ppdn-digital-watch-men/p/itme34fz4dejhbes?pid=WATE34FM4B65YDDE",
          "http://www.flipkart.com/maxima-26280cmli-attivo-analog-watch-women/p/itmdsv44dfe7sa42?pid=WATDSV3UZED5XFHA",
          "http://www.flipkart.com/maxima-17321cmly-gold-analog-watch-women/p/itmdyfq6wwfsr6ym?pid=WATDYFQ559FZWRSQ",
          "http://www.flipkart.com/natures-plus-home-garden-plant-container-set/p/itme293ydtzcq4nx?pid=PCSE27VV35ZGZBB3",
          "http://www.flipkart.com/global-nomad-gnlbbl0314-analog-watch-men/p/itmdzrzkqqzc66en?pid=WATDZRZGCSSQ8RYS",
          "http://www.flipkart.com/agricart-african-marigold-vanilla-f1-white-seed/p/itme8ahwjhufghyc?pid=PAEE8AHWJWMDAXZU",
          "http://www.flipkart.com/sonata-7007yl09-essentials-analog-watch-men/p/itmdg9fym9rh8wra?pid=WATDG9F7SDHKQNRJ",
          "http://www.flipkart.com/sonata-87001sl01-analog-watch-women/p/itmdnauchn4qbuge?pid=WATDNAUBP94U2VZE",
          "http://www.flipkart.com/fluid-fs209-bk01-digital-watch-men/p/itmeyg9zfuphb5ra?pid=WATEYG9YBGAFF7BA",
          "http://www.flipkart.com/maxima-21101bmly-gold-analog-watch-women/p/itmdhukcwqkhcbfh?pid=WATDHUKBGWGCHQQX",
          "http://www.flipkart.com/fastrack-9770pl01-sport-analog-watch-women/p/itmd9x3eg8fbfnyj?pid=WATD9XFGAJQGR4AQ",
          "http://www.flipkart.com/vgreen-plant-container-set/p/itme9r3ubqwcbb32?pid=PCSE9R3UWEMF57RQ",
          "http://www.flipkart.com/blessed-ring-plant-container-set/p/itmdy5axh37gtgj3?pid=PCSDY5AHUNGBYFXH",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5ax7k5wpb9z?pid=PCSDY5AFQE42NNTK",
          "http://www.flipkart.com/maxima-22381bmly-gold-analog-watch-women/p/itmdunhgjzrndbzj?pid=WATDUNJ7AZ9RYTAF",
          "http://www.flipkart.com/fastrack-9298pv06-beach-analog-watch-men/p/itmdazzk9xhuhkbb?pid=WATDAZPXK8FSPGB4",
          "http://www.flipkart.com/maxima-29923lpgy-analog-watch-men/p/itmeyy4x4vchq7kq?pid=WATEYY4X2SYPGHSX",
          "http://www.flipkart.com/sonata-77018pl01-watch/p/itme6nvszdynvgf7?pid=WATE6NVSM2KFHF2R",
          "http://www.flipkart.com/maxima-20981lmgi-attivo-analog-watch-men/p/itme4s5wqmrfxmgs?pid=WATE4S5RKYHT9W3Z",
          "http://www.flipkart.com/agricart-lettuce-seed/p/itme8ndk6hahwjfw?pid=PAEE8NDKFTPRKYMU",
          "http://www.flipkart.com/maxima-24742lmgy-gold-analog-watch-men/p/itmdhmsjjugrmyja?pid=WATDHMQJ68MVBRFV",
          "http://www.flipkart.com/sonata-8974pp03-analog-watch-women/p/itmdgdg8kzjzs6xg?pid=WATDGDHYCPR2PPSK",
          "http://www.flipkart.com/natures-plus-home-garden-plant-container-set/p/itme4fkcyzbxkrnz?pid=PCSE4FKCKZZMHKYG",
          "http://www.flipkart.com/timewel-1100-n498-analog-watch-men/p/itmey7sdz4frj4d8?pid=WATEY7SDM6TDEZCK",
          "http://www.flipkart.com/maxima-26092pmgb-attivo-analog-watch-men/p/itmdjtskrjeyykpy?pid=WATDJTR9BN4BB5AJ",
          "http://www.flipkart.com/maxima-24460cmgi-attivo-analog-watch-men/p/itmdjtskv45cvza5?pid=WATDJTR9ADKGNP68",
          "http://www.flipkart.com/noise-nosww001-analog-watch-men-women/p/itmdffj7kkyz3bnp?pid=WATDFFH3KJYBTYGG",
          "http://www.flipkart.com/yuccabe-italia-stella-yellow-self-watering-planter-plant-container-set/p/itme4tf3gae8jqhv?pid=PCSE4SFFJSWJZVH4",
          "http://www.flipkart.com/sf-sonata-7991pp02-ocean-digital-watch-men/p/itmdg9fyr3nurdnw?pid=WATDG9F723NCPXNU",
          "http://www.flipkart.com/fluid-fu203-gr01-analog-digital-watch-men/p/itmduk7dv6gstkrd?pid=WATDUK7DV6GSTKRD",
          "http://www.flipkart.com/maxima-06362cmgy-gold-analog-watch-men/p/itmdjtskuhdzywgy?pid=WATDJTR93NB8HHQC",
          "http://www.flipkart.com/blessed-plain-plant-container-set/p/itmdy5axpfgcezrh?pid=PCSDY5AHEENB3Q9X",
          "http://www.flipkart.com/klick-solid-women-s-tunic/p/itmefkjf2tjwedfz?pid=TUNEFKJFT6H4JTHG",
          "http://www.flipkart.com/fastrack-nd9915pp05j-teevirus-analog-watch-women-men/p/itmdkb7z2bhzmzr9?pid=WATDKB7JW7USDVZ6",
          "http://www.flipkart.com/sonata-8925yl02-analog-watch-women/p/itmeyfrkp8ydtkmc?pid=WATDZ2ZQGEYGQCFX",
          "http://www.flipkart.com/petrol-pfwbl60-analog-watch-men/p/itmdtwrzksxqcxdp?pid=WATDTWRZKSXQCXDP",
          "http://www.flipkart.com/sonata-8944sl03-analog-watch-women/p/itmdz2zsbrc6vhu8?pid=WATDZ2ZQYNBVMVGD",
          "http://www.flipkart.com/fastrack-9914pp05-tees-analog-watch-women-men/p/itmd9x3ehpfuqajf?pid=WATD9XFGSYPAUWG7",
          "http://www.flipkart.com/sonata-7078yl04-fiber-collection-analog-watch-men/p/itmdz2zs3ddekhkh?pid=WATDZ2ZQTPKQZEHG",
          "http://www.flipkart.com/maxima-07591ppgw-aqua-analog-watch-men/p/itmdvjntxg2ryeth?pid=WATDVJNATRBF2C3W",
          "http://www.flipkart.com/sonata-7097sm01-analog-watch-men/p/itmdgfdkzkkpgxdt?pid=WATDGFAQCFCVSJPA",
          "http://www.flipkart.com/joy-living-garden-plant-container-set/p/itmdy5axvkfcvm7k?pid=PCSDY5AFPWQBABVU",
          "http://www.flipkart.com/sir-time-st05-bk01-digital-watch-men/p/itmefr35kmufhw3u?pid=WATEFR35RSGBNGWW",
          "http://www.flipkart.com/maxima-28393lmli-attivo-analog-watch-women/p/itmdnv4vgugkm6zm?pid=WATDNV3VGWQEVHJU",
          "http://www.flipkart.com/maxima-20183cmgi-attivo-analog-watch-men/p/itmd9gjfwnrgb33w?pid=WATD9H76RKGUUZHY",
          "http://www.flipkart.com/fastrack-9333pp04-analog-watch-men/p/itmdg4hdpky2dxup?pid=WATDG4KP445AV5XC",
          "http://www.flipkart.com/sonata-7093sl02-yuva-analog-watch-men/p/itmda5wa3ynsejbq?pid=WATDA5ZAG2DH6D2R",
          "http://www.flipkart.com/sonata-8013yl02-analog-watch-women/p/itmdg9fyybbdw4wt?pid=WATDG9F7KNFKTDCF",
          "http://www.flipkart.com/noise-nosww028-round-dial-jelly-analog-watch-men-women/p/itmdjyqjhgyzzarm?pid=WATDJYPXKHPPNGQK",
          "http://www.flipkart.com/sonata-7007yl07-analog-watch-men/p/itmdz2zrgzazgpwh?pid=WATDZ2ZQNBEYZEWR",
          "http://www.flipkart.com/ne-shoes-women-wedges/p/itme9hrvqskzbqza?pid=SNDE9HRW9ZVPG9A6",
          "http://www.flipkart.com/maxima-25703ppkw-fiber-analog-watch-women/p/itmdp5nhgxbzyzfq?pid=WATDP5NHXYENPWQW",
          "http://www.flipkart.com/sneha-unique-women-wedges/p/itme7vefgbfqzvqs?pid=SNDE7VEFHDQF8QRS",
          "http://www.flipkart.com/first-smart-deal-plant-container-set/p/itmeayrtrfjkuhqz?pid=PCSEAYRTUYVYYC6Y",
          "http://www.flipkart.com/maxima-05660ppgw-analog-watch-men-women/p/itmeyy4x5qyz7jbx?pid=WATEYY4XQ4GEP7HV",
          "http://www.flipkart.com/maxima-13881ppgw-fiber-collection-analog-watch-men/p/itmdjtskcfytvrz3?pid=WATDJTR979TAXJJZ",
          "http://www.flipkart.com/sonata-8925ym05-analog-watch-women/p/itmdk2hunh6zxchs?pid=WATDK2G2WM5XHF9S",
          "http://www.flipkart.com/sonata-7011sm05-yuva-analog-watch-men/p/itmda5wauzfrexfu?pid=WATDA5ZAXAP2VTGQ",
          "http://www.flipkart.com/maxima-24864lmgy-analog-watch-men/p/itme26j8jheahgya?pid=WATE26J7ZMQDQGZN",
          "http://www.flipkart.com/maxima-10310lmgi-attivo-analog-watch-men/p/itmdjtsk7ruytuzh?pid=WATDJTR9HJQGBGWG",
          "http://www.flipkart.com/maxima-23237ppgn-fiber-collection-analog-watch-men/p/itmdgnavzpvyafzg?pid=WATDGNATHYWSGVE8",
          "http://www.flipkart.com/e-plant-spicy-chillie-seed/p/itme7a8qfrjgkrfk?pid=PAEE7A8QVZTNQBBY",
          "http://www.flipkart.com/maxima-04608cmgy-gold-analog-watch-men/p/itmdz5hgcffzfdyw?pid=WATDZ5HGXEYDHBWD",
          "http://www.flipkart.com/only-kidz-20581-barbie-digital-watch-women/p/itmdwabsmjmttu3y?pid=WATDWABR2QMHU2YK",
          "http://www.flipkart.com/sonata-7092sl01-yuva-analog-watch-men/p/itmda5wabnyfzq2w?pid=WATDA5ZABPHZZV3Q",
          "http://www.flipkart.com/stol-n-kids-time01-1-tweety-analog-watch-girls-boys/p/itmduguzabnt4rrt?pid=WATDUGUZABNT4RRT",
          "http://www.flipkart.com/natures-plus-home-garden-plant-container-set/p/itme4fkc37rydyng?pid=PCSE4FKCFUXFP9VW",
          "http://www.flipkart.com/sonata-7924sl03-sport-casual-analog-watch-men/p/itmda5wafehhhhzh?pid=WATDA5ZAHQJNHKJV",
          "http://www.flipkart.com/maxima-26512ppgn-fiber-collection-analog-watch-men/p/itmdjtskkfuwabxz?pid=WATDJTR9HKKRXKTJ",
          "http://www.flipkart.com/maxima-20681lpli-swarovski-analog-watch-women/p/itmdz5hhu3r3wqyz?pid=WATDZ5HGWG5B5ZWM",
          "http://www.flipkart.com/sonata-7970sl05-watch/p/itmdz2zs2qh9qg4b?pid=WATDZ2ZQWKH2ERZ9",
          "http://www.flipkart.com/e-plant-plant-container-set/p/itme3yffcq9zx2qc?pid=PCSE3YFFCYQVRNYX",
          "http://www.flipkart.com/maxima-01427cmgy-gold-analog-watch-men/p/itmdyfq6wthm8xmr?pid=WATDYFQ5664GGDGN",
          "http://www.flipkart.com/maxima-20020lmgi-attivo-analog-watch-men/p/itmd9gjfvggszspg?pid=WATD9H76UXEZHVUF",
          "http://www.flipkart.com/petrol-pcwbl68-analog-watch-men/p/itmdpv5yjbbcvdzh?pid=WATDPV5TUCGZ8JCN",
          "http://www.flipkart.com/onlineshoppee-plant-container-set/p/itme4q73bnmuwjpw?pid=PCSE4Q73ZVYGCYMF",
          "http://www.flipkart.com/flippd-fdrbb1814-fibre-analog-watch-men/p/itmeyuzymj62mbgm?pid=WATEYUZXGBYVBF24",
          "http://www.flipkart.com/sonata-7958pp01-analog-watch/p/itmdp5vzgwyeehsg?pid=WATDP5VZZQPZSNZW",
          "http://www.flipkart.com/flippd-fd040103-formal-analog-watch-men-boys/p/itme8e8pxpzmeyyh?pid=WATE8E8PMU6ZRZGZ",
          "http://www.flipkart.com/kielz-women-wedges/p/itme3vt3quhwv5cj?pid=SNDE3VT3MMFHKD4Z",
          "http://www.flipkart.com/natures-plus-home-garden-plant-container-set/p/itme293y7nk5qy3e?pid=PCSE27VWRYYZMNZE",
          "http://www.flipkart.com/maxima-20141cmgi-attivo-analog-watch-men/p/itmd9gjfjqzgbbvp?pid=WATD9H76RG5FQT5Y",
          "http://www.flipkart.com/only-kidz-20238-barbie-analog-watch-boys-girls/p/itmd9gjfhe2z3pj7?pid=WATD9H76VEZPMPCK",
          "http://www.flipkart.com/only-kidz-20600-digital-watch-boys-girls/p/itmdwabswftyvdgk?pid=WATDWABRFCWT2DD3",
          "http://www.flipkart.com/flippd-fdlwbr3714-fashion-analog-watch-men/p/itmefwp45v98gjbx?pid=WATEFWP4V5ZEHZZY",
          "http://www.flipkart.com/sonata-8097ym01-analog-watch-women/p/itmdwgamgmzwcbpt?pid=WATDWGAHMR6NHPWB",
          "http://www.flipkart.com/kool-kidz-dmk-011-pk-01-analog-watch-boys-girls/p/itmdwbhu7vkhygxa?pid=WATDWBHR38VKQAKG",
          "http://www.flipkart.com/noise-nosww025-round-dial-jelly-analog-watch-men-women/p/itmdjyqjhe5fm8ry?pid=WATDJYPXGCMMFZCX",
          "http://www.flipkart.com/nexus-nx-7570-analog-watch-women/p/itmdxfgt8agvmav2?pid=WATDXFGTHYZXYY4N",
          "http://www.flipkart.com/aadi-alloy-metal-bangle/p/itmdr6bmzzgdv5qe?pid=BBADR6BH7Y9CTAEH",
          "http://www.flipkart.com/maxima-29182cmgi-attivo-analog-watch-men/p/itmdunhh7xzy6th7?pid=WATDUNJ7VGBH2HJ3",
          "http://www.flipkart.com/petrol-pcbbl67-analog-watch-men/p/itmdtwrzqaschsmk?pid=WATDTWRZQASCHSMK",
          "http://www.flipkart.com/maxima-20250bmli-swarovski-analog-watch-women/p/itmdtdzyfrrczrty?pid=WATDTDZGVUUNFPYD",
          "http://www.flipkart.com/fastrack-nd3062pp08-tees-analog-watch-men-women/p/itmdkb7zdxwfcvay?pid=WATDKB7JEE3WAZUE",
          "http://www.flipkart.com/sir-time-st01-sybk-digital-watch-men/p/itmdzdgtvz7f9rjd?pid=WATDZDGRHWMT3DH8",
          "http://www.flipkart.com/maxima-01727lpln-mac-gold-analog-watch-women/p/itmdz5hgayzz8zur?pid=WATDZ5HGF7WGCFGH",
          "http://www.flipkart.com/kool-kidz-dmk-001-pr-01-analog-watch-boys-girls/p/itmdqyqypgha2ffe?pid=WATDPV5TVAPYZCJA",
          "http://www.flipkart.com/hmt-g5141-watch-men/p/itmdqg96vajzjvfq?pid=WATDHHASRYSYZGQV",
          "http://www.flipkart.com/ortho-rest-women-flats/p/itmebcqzknqp2bxf?pid=SNDEBCQZHYXUYHPN",
          "http://www.flipkart.com/maxima-27280ppgw-fiber-analog-watch-men/p/itmdp5nh5gfbewny?pid=WATDP5NHENJGYYXF",
          "http://www.flipkart.com/hmt-s3648-analog-watch-men/p/itmdyq93zcnqpkt7?pid=WATDYQ93UUZYVFQX",
          "http://www.flipkart.com/nell-women-flats/p/itme5e6bfnhvwyth?pid=SNDE5E6BCHZCC7JQ",
          "http://www.flipkart.com/nexus-nx-7591-analog-watch-women/p/itmdxfgtrzxyrazh?pid=WATDXFGTREYMG4ZW",
          "http://www.flipkart.com/only-kidz-20368-digital-watch-boys-girls/p/itmdtjszbdcepy9b?pid=WATDDAYYPCVYBPYE",
          "http://www.flipkart.com/sonata-8098ym01-analog-watch-women/p/itmdz2zsdh7hfydw?pid=WATDZ2ZQAFGKBF2Z",
          "http://www.flipkart.com/noise-nosww026-round-dial-jelly-analog-watch-men-women/p/itmdjyqjefatmc4d?pid=WATDJYPXZMUSCBJN",
          "http://www.flipkart.com/fastrack-3062pp09-tees-pop-analog-watch-men-women/p/itmdewzahhtdzahn?pid=WATDEWZ9UMDYPWYC",
          "http://www.flipkart.com/fastrack-9912pp15-tees-analog-watch-men-women/p/itmddxffs3fzzz5q?pid=WATDDXF3D4SGXCW8",
          "http://www.flipkart.com/sonata-8974pp01-analog-watch-women/p/itmdjykjjwy5aphu?pid=WATDGDHYHGDPZNCX",
          "http://www.flipkart.com/sonata-8943yl03-yuva-gold-analog-watch-women/p/itmda5waztatephz?pid=WATDA5ZAWCTQHAY4",
          "http://www.flipkart.com/sonata-8925ym06j-analog-watch-women/p/itmdp98gufthgsur?pid=WATDP98GNAWTNAEJ",
          "http://www.flipkart.com/sonata-7089sl01-yuva-analog-watch-men/p/itmda5wahhmyfrah?pid=WATDA5ZAYCZRQQXH",
          "http://www.flipkart.com/sonata-7007sl02-analog-watch-men/p/itmdwgam7yq7ejuw?pid=WATDWGAHRCPFYWGW",
          "http://www.flipkart.com/hmt-sonata-gold-plated-watch-men-analog/p/itmdznshqxeauht8?pid=WATDZNSHJHDTS9GN",
          "http://www.flipkart.com/global-nomad-gnlwbr0114-analog-watch-men/p/itmdzrzkrtvmhygq?pid=WATDZRZGZAM7HDGV",
          "http://www.flipkart.com/times-sd-147-casual-analog-watch-women/p/itme7f5j2u6szgt7?pid=WATE7F5JK2JFFHD5",
          "http://www.flipkart.com/noise-nosww030-m-famous-analog-watch-men-women/p/itmdjyqj3tskrsxz?pid=WATDJYPXTT4DQARH",
          "http://www.flipkart.com/aashka-women-wedges/p/itmey8phs5hpyx9h?pid=SNDEY8PHWKQCADZD",
          "http://www.flipkart.com/get-glamr-women-wedges/p/itme56uuhzkuhfug?pid=SNDE56UUKGHHWFGF",
          "http://www.flipkart.com/fastrack-9297pp01-sports-analog-watch-men/p/itmd9gjffrhpfu4f?pid=WATD9H766HFJKMBM",
          "http://www.flipkart.com/get-glamr-women-wedges/p/itme56uuug56dhmq?pid=SNDE56UUTHBTQMQ2",
          "http://www.flipkart.com/fastrack-9913pp03-tees-analog-watch-women/p/itmd9gjfyf67cvzf?pid=WATD9H76YMYPCMCK",
          "http://www.flipkart.com/sonata-8076yl01-analog-watch-women/p/itmdbrx7htfcebvx?pid=WATDBRSFAY6UKWMJ",
          "http://www.flipkart.com/alto-moda-pantaloons-solid-women-s-tunic/p/itmea4dtzus2uzrz?pid=TUNEA4DTPGMEGRAS",
          "http://www.flipkart.com/maxima-19413ppsn-fiber-collection-digital-watch-men/p/itmd9gjfr37tncfc?pid=WATD9H76QFGFQAHV",
          "http://www.flipkart.com/sonata-everyday-analog-watch-women/p/itmdffj7dy5fdefn?pid=WATDFFH3RVHGTBR3",
          "http://www.flipkart.com/nexus-nx-7557-analog-watch-women/p/itmdxfgtxnzfnefd?pid=WATDXFGTP3FEMGEH",
          "http://www.flipkart.com/flippd-fddc03-analog-watch-men/p/itme3yhmt6mqp6be?pid=WATE3YHHPC4ZBWZ8",
          "http://www.flipkart.com/maxima-07035lmli-attivo-analog-watch-women/p/itmdhukce3cxdkdp?pid=WATDHUKBNTNDRZ4Q",
          "http://www.flipkart.com/fastrack-9912pp18-tees-analog-watch-men-women/p/itmddxffcmdkbqwr?pid=WATDDXF3B7QGT3MC",
          "http://www.flipkart.com/fastrack-9331pp01-basics-analog-watch-men/p/itmd9gjg8yaknyhy?pid=WATD9H76GF3QFV22",
          "http://www.flipkart.com/maxima-29081lmgi-attivo-analog-watch-men/p/itmdunhhfqwshjzk?pid=WATDUNJ7PGYUWDGQ",
          "http://www.flipkart.com/maxima-19883bmli-swarovski-analog-watch-women/p/itmde9nrsuhz9dg8?pid=WATDE9NFPB9TBVSK",
          "http://www.flipkart.com/hmt-b022-hq-analog-watch-women/p/itmdhhasbe65efs7?pid=WATDHHASYQHYZH2H",
          "http://www.flipkart.com/sonata-8925ym06-analog-watch-women/p/itmdwgamdym6hatm?pid=WATDWGAHG7AHMW6Y",
          "http://www.flipkart.com/flippd-fd15102-analog-watch-men/p/itme3hwh5zdbq5qp?pid=WATE3HFNNASZJQYH",
          "http://www.flipkart.com/kool-kidz-dmk-011-bk-01-analog-watch-girls-boys/p/itmdwbhuzhxhnusj?pid=WATDWBHRJHAHKCWG",
          "http://www.flipkart.com/hmt-olss-01-analog-watch-women/p/itmdvgj8wtjazehq?pid=WATDVGGHWZBHXYBS",
          "http://www.flipkart.com/fastrack-9792pp02-basics-analog-watch-women/p/itmd9gjffvqmn8sn?pid=WATD9H76N5WQYVGJ",
          "http://www.flipkart.com/flippd-fdrbb2114-fibre-analog-watch-men/p/itmeyuzyn2bdc8jq?pid=WATEYUZXUHBBRZD6",
          "http://www.flipkart.com/noise-nosww014-grip-analog-watch-men-women/p/itmdjyqjghfnwpkg?pid=WATDJYPXRGYP5XVT",
          "http://www.flipkart.com/sonata-8082sl01-analog-watch-women/p/itmdgfdkmyedyjna?pid=WATDGFAQBJJV2TTK",
          "http://www.flipkart.com/maxima-29126lmgy-gold-analog-watch-men/p/itme4s5vtxctrtha?pid=WATE4S5RKVGMKTRQ",
          "http://www.flipkart.com/nexus-nx-7690-analog-watch-women/p/itmdxfgtw9htmscf?pid=WATDXFGTBUZJVTZQ",
          "http://www.flipkart.com/maxima-19884lmli-swarovski-analog-watch-women/p/itmd9gjfguhdqbzb?pid=WATD9H76PTHAUCHY",
          "http://www.flipkart.com/maxima-05712lmly-analog-watch-women/p/itme26j8yctrgwfj?pid=WATE26J7DTHUYJN8",
          "http://www.flipkart.com/fastrack-9827pp10-analog-watch-women/p/itmdg4hdehznh78a?pid=WATDG4KPSFPXYPSR",
          "http://www.flipkart.com/sonata-8076yl02-analog-watch-women/p/itmdbrx7hm5hbjja?pid=WATDBRSF9CKTYBB7",
          "http://www.flipkart.com/maxima-05711lmly-gold-analog-watch-women/p/itmdz5hgg2mqtzv4?pid=WATDZ5HGGUGHEZMH",
          "http://www.flipkart.com/hmt-olss-03-analog-watch-women/p/itmdvgj8z36cnhdk?pid=WATDVGGHNSHKU4ED",
          "http://www.flipkart.com/fastrack-3062pp12-tees-pop-analog-watch-women-men/p/itmdewzahzhmjjb7?pid=WATDEWZ9KHPSHESC",
          "http://www.flipkart.com/fastrack-3062pp19-tees-analog-watch-men-women/p/itmdewzaxh9yhjbj?pid=WATDEWZ9UHSEHGZG",
          "http://www.flipkart.com/maxima-25014lmgi-attivo-analog-watch-men/p/itme26j8zewnwduk?pid=WATE26J74MGUBFFB",
          "http://www.flipkart.com/flippd-fd040107-casual-analog-watch-men-boys/p/itme8e8p7hggzgew?pid=WATE8E8PFRKYYXQP",
          "http://www.flipkart.com/fastrack-nd9912pp04j-analog-watch-women-men/p/itmdkb7zzn7ke5gz?pid=WATDKB7JHUHHVMU9",
          "http://www.flipkart.com/flippd-fdrbb2814-orange-fibre-analog-watch-men/p/itmeyuzymqmh6asr?pid=WATEYUZXN2DHGZ36",
          "http://www.flipkart.com/timewel-1100-n1944-b-analog-watch-women/p/itme2fagcvxsgh8d?pid=WATE2FAGESM5B5VZ",
          "http://www.flipkart.com/flippd-fdrbb1614-fibre-analog-watch-men/p/itmeyuzyqba7qnut?pid=WATEYUZXWKUESAYZ",
          "http://www.flipkart.com/timewel-1100-n1508-analog-watch-women/p/itmeyap3k4z7afm6?pid=WATEYAP3K2QQQWDH",
          "http://www.flipkart.com/maxima-07138cmgy-analog-watch-men/p/itme26j8fguhbzbk?pid=WATE26J747RNXYG7",
          "http://www.flipkart.com/sf-sonata-7963pp02-dean-analog-watch-men/p/itmda5wawhpzycxp?pid=WATDA5ZA3Z3UJJJQ",
          "http://www.flipkart.com/flippd-fddc04-analog-watch-men/p/itme3yhmbachp9ud?pid=WATE3YHHFFCUGZFB",
          "http://www.flipkart.com/sonata-8024sl10-yuva-analog-watch-women/p/itmda5wagfg4gprt?pid=WATDA5ZA3R73RZWC",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itmeahmsteqxm8es?pid=BRAEGJFXV7XKSGA2",
          "http://www.flipkart.com/body-balance-imon-energy-wristband/p/itmdz2xxgtjakp3n?pid=BANDNHT9FSHKAEYM",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8vp6r6fxhxa2?pid=BRAEGJFXUHYZPDWZ",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb972bz398gzz?pid=BRAEGJFXSM9ZQ6SK",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8z2hvz9hrvyy?pid=BRAEGJFX4TT4SEGR",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96shpdkygvj?pid=BRAEGJFX2VW8NSMP",
          "http://www.flipkart.com/naughty-ninos-girl-s-white-pink-dungaree/p/itme785uccghrpzn?pid=DRPEEZNFGG9J9KAV",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itmeahmspqnhpfch?pid=BRAEGJFXCXSJJF6Z",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme87fybhzfxpsa?pid=BRAEGJFXESES6E8F",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96s8zgfbnbz?pid=BRAEGJFXYJXQYESX",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8z2m5qgdsayd?pid=BRAEGJFXJR4GPU2C",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96saupthpfn?pid=BRAEGJFXYTH2MG98",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8z2fgcgzfvzt?pid=BRAEGJFXUBWQFBCS",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itmeahmsaqhgbwmx?pid=BRAEGJFXUBNKSKZZ",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96stfwkzndv?pid=BRAEGJFX4ZCMZHH6",
          "http://www.flipkart.com/woly-smooth-leather-shoe-cream/p/itmdhfx3vhhrczp3?pid=SPMDHEZ4GT8R8HCH",
          "http://www.flipkart.com/metmo-slippers/p/itmeg63ypqss3222?pid=SFFEG763F38URMXA",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96stzdzhba6?pid=BRAEGJFX7PSVECHP",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmebfd7gxty9fzm?pid=BRAEGJFXKH8YPEZZ",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itmeb3tqarxybpem?pid=BRAEGJFXSUDSP8H3",
          "http://www.flipkart.com/pu-good-women-flats/p/itmeghuuc5mmn4dz?pid=SNDEGHUUHYK7D48R",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme9q9yhv3esxp7?pid=BRAEGJFXW54GVEFH",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96skfhg4xyk?pid=BRAEGJFXNGCKADF6",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb972jjwmgfyy?pid=BRAEGJFXWMKWGTG5",
          "http://www.flipkart.com/clovia-women-s-t-shirt-bra/p/itmeb96szhumqnct?pid=BRAEGJFXGYFPGHYG",
          "http://www.flipkart.com/clovia-women-s-plunge-bra/p/itmed7euhahpwgpe?pid=BRAEGJFXHYTGZ2QC",
          "http://www.flipkart.com/decore-sources-assorted-artificial-plant-pot/p/itmeemcanhpbxzzh?pid=ARPEEMCAMGADRCGQ",
          "http://www.flipkart.com/subh-akriti-assorted-artificial-plant/p/itmedqm3uqmgx6bx?pid=ARPEDQM39KH99YSG",
          "http://www.flipkart.com/klick-casual-formal-party-sleeveless-solid-women-s-top/p/itmeyp87pxaahzxj?pid=TOPEYP876AAGE9NC",
          "http://www.flipkart.com/hepburnette-women-heels/p/itme7nstm6b9gw3q?pid=SNDE7NSTNHAEACGG",
          "http://www.flipkart.com/perky-girl-s-layered-dress/p/itme9qsvzajp7yxa?pid=DREE9QSVADZEKNJS",
          "http://www.flipkart.com/veakupia-casual-sleeveless-solid-women-s-top/p/itme96848xmsfnzp?pid=TOPE9684RQWWZFTV",
          "http://www.flipkart.com/cutecumber-girl-s-a-line-dress/p/itme4fc4z6nzqhyk?pid=DREE4FC4TAR8M5GN",
          "http://www.flipkart.com/cutecumber-girl-s-a-line-dress/p/itme4fc4s5gu4vzf?pid=DREE4FC46AXGNA5V",
          "http://www.flipkart.com/rann-women-s-leggings/p/itmea3hfdgzth7za?pid=LJGEA3HFG2YDEWDC",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itme4dngjtr4j7un?pid=TSHE4DNGZFWK6GYR",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeegh2gadnre5f?pid=TSHE4DNGWNY3TE4B",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeegh3apnw3shf?pid=TSHE5YZC5ZFJYPR2",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeegh2xvq2amrm?pid=TSHE4DTF53HPYMU4",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeegh22rckpebw?pid=TSHE4S26ZSFE9JTB",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeegh2qa8cyy6v?pid=TSHE4S26RPZTXB7R",
          "http://www.flipkart.com/campusmall-printed-men-s-round-neck-t-shirt/p/itmeeghfvgzj2yhy?pid=TSHE4ENHQHZYRNYZ",
          "http://www.flipkart.com/perky-girl-s-layered-dress/p/itmea8zptfurxr6v?pid=DREEA8ZPVQDYZYR6",
          "http://www.flipkart.com/nun-printed-women-s-broomstick-skirt/p/itme2t2yh9yzwd3m?pid=SKIE2T2YHZFNXCDH",
          "http://www.flipkart.com/vanca-formal-3-4-sleeve-printed-women-s-top/p/itmean43zszheptv?pid=TOPEAN43YRRX5X5G",
          "http://www.flipkart.com/veakupia-casual-full-sleeve-solid-women-s-top/p/itme7t5fcezhg6wp?pid=TOPE7T5FMBVW9EFY",
          "http://www.flipkart.com/kaizer-jewelry-stainless-steel-zircon-ring/p/itme3nfsgqy4rcff?pid=RNGE3NFSNCUBC3QM",
          "http://www.flipkart.com/i-kitpit-pouch-lenovo-a369i/p/itmdxh5jweqqfd7g?pid=ACCDXH5JWYYPBBGC",
          "http://www.flipkart.com/i-kitpit-pouch-lenovo-a369i/p/itmdxf9hg6ptkddu?pid=ACCDXF9HT5SHRYYE",
          "http://www.flipkart.com/i-kitpit-pouch-lenovo-a369i/p/itmdxh5jhvutchv6?pid=ACCDXH5JXWABF7GH",
          "http://www.flipkart.com/puma-casual-short-sleeve-printed-women-s-top/p/itmdsgusswmp6cxj?pid=TOPDSGUSBSDSRXVJ",
          "http://www.flipkart.com/ciemme-0-11-ct-women-s-designer-circle-flower-promise-yellow-gold-diamond-18-k-ring/p/itme96yfuxeznacf?pid=RNGE96Y2KTQSGHNG",
          "http://www.flipkart.com/dewberries-formal-short-sleeve-self-design-women-s-top/p/itmeccnuu5vbsqaj?pid=TOPECENJ85HRQQHA",
          "http://www.flipkart.com/zink-london-casual-sleeveless-solid-women-s-top/p/itme5mce6agrpgyr?pid=TOPE5MCE7YUGFMHY",
          "http://www.flipkart.com/zink-london-casual-full-sleeve-printed-women-s-top/p/itme5uvfcbmsrhbz?pid=TOPE5W325WWQFR3B",
          "http://www.flipkart.com/zink-london-casual-short-sleeve-solid-women-s-top/p/itme6qgaqsezwzey?pid=TOPE6QGAWN9YDQWZ",
          "http://www.flipkart.com/today-fashion-casual-3-4-sleeve-solid-women-s-top/p/itmeb7bffjhkghsr?pid=TOPEB7BFCW7YG7KG",
          "http://www.flipkart.com/highlander-men-s-solid-casual-shirt/p/itme9c3vjkgutete?pid=SHTE9C3VMAASRH33",
          "http://www.flipkart.com/highlander-men-s-printed-casual-shirt/p/itmedzy5pybqzagn?pid=SHTEDZY5RMB5ZZVG",
          "http://www.flipkart.com/mk-teddy-minion-double-eye-35-cm/p/itmebczqdczryx2g?pid=STFEBCZQ5YYZJYSG",
          "http://www.flipkart.com/imbindass-printed-men-s-round-neck-t-shirt/p/itmecpzrghfgyrat?pid=TSHECPZRPFMWUTGJ",
          "http://www.flipkart.com/royal-diamond-jewellery-charisma-gold-yellow-gold-14-k-ring/p/itme4z3djtphvrmp?pid=RNGE4Z3DDZ3YAKSG",
          "http://www.flipkart.com/wearyourshine-pcj-nitza-diamond-gold-yellow-18-k-ring/p/itmeyfh6a9jdjz9q?pid=RNGEYFH7FFZBBHCB",
          "http://www.flipkart.com/craftter-flying-butterfly-square-wall-lamp/p/itme6g7ck37qzphb?pid=TLPE6G7CW7ANM9WT",
          "http://www.flipkart.com/popnetic-casual-short-sleeve-solid-women-s-top/p/itme8s7qzfx98uwv?pid=TOPE8S7QPKHRWNHE",
          "http://www.flipkart.com/avenue-analog-wall-clock/p/itmec8aggxeggerm?pid=WCKEC8AG8EYWFSA7",
          "http://www.flipkart.com/sparkle-street-brass-enamel-bangle-set/p/itme4br6qnnazgkt?pid=BBAE4BR6QAUEK73K",
          "http://www.flipkart.com/alda-3-ply-ss-lid-pan-26-cm-diameter/p/itmdvrh4qfjkgtbr?pid=PTPDVPEXQ88YHBEE",
          "http://www.flipkart.com/do-bhai-women-flats/p/itme2rsf5nq2ay4u?pid=SNDE2RSFZ7Y3G7Y8",
          "http://www.flipkart.com/bagsy-malone-hand-held-bag/p/itme2h8g6a9dv8xy?pid=HMBE2H8GSPFJAFFZ",
          "http://www.flipkart.com/baklol-printed-men-s-round-neck-t-shirt/p/itme8khyyvasyxpw?pid=TSHE8KHYFHKXHRXX",
          "http://www.flipkart.com/hp-15-ac116tx-notebook-core-i3-5th-gen-4gb-1tb-win10-2gb-graph-n8m19pa/p/itmeaz946ex4qern?pid=COMEAZ945RHFFGUS",
          "http://www.flipkart.com/hp-15-ac121tu-notebook-core-i3-5th-gen-4gb-1tb-win10-n8m17pa/p/itmeaz943ex2hknx?pid=COMEAZ94HWYQTZHZ",
          "http://www.flipkart.com/puma-men-s-striped-casual-shirt/p/itmddh49dgcq674z?pid=SHTDCFZRMHZFFUK3",
          "http://www.flipkart.com/sayitloud-printed-men-s-round-neck-t-shirt/p/itme6sjfc9dwavxg?pid=TSHE6SJFFQUMVYBH",
          "http://www.flipkart.com/4thneed-solid-men-s-polo-t-shirt/p/itme535mhq2mtdyv?pid=TSHE535MZ5CVFQ8F",
          "http://www.flipkart.com/baklol-printed-men-s-round-neck-t-shirt/p/itme8jzhubbtfb5m?pid=TSHE8JZHJPUPWDKZ",
          "http://www.flipkart.com/baklol-printed-men-s-round-neck-t-shirt/p/itme8gghpedwcnmj?pid=TSHE8GGHEMKPZHGH",
          "http://www.flipkart.com/dna-graphic-print-men-s-round-neck-t-shirt/p/itme6kzzjbgz5yu2?pid=TSHE6KZZQ7BGSSQE",
          "http://www.flipkart.com/docare-women-s-sports-bra/p/itmefwhaudhmtzzm?pid=BRAEFWHAV6EWJFBC",
          "http://www.flipkart.com/rawpockets-graphic-print-men-s-round-neck-t-shirt/p/itme7g83zsredmzj?pid=TSHE7G83RZVRTTBB",
          "http://www.flipkart.com/baklol-printed-men-s-round-neck-t-shirt/p/itme8khyg8vqzfnw?pid=TSHE8KKZRMHYY5T6",
          "http://www.flipkart.com/dna-graphic-print-men-s-round-neck-t-shirt/p/itme6zf3kzvgm62v?pid=TSHE6ZF3FTCBWT4R",
          "http://www.flipkart.com/ilo-women-heels/p/itme2pq4ywr8jjza?pid=SNDE2PQ45GJSGYKB",
          "http://www.flipkart.com/lyc-women-heels/p/itme4bhtgtexvwka?pid=SNDE4BHTMEG9GUMX",
          "http://www.flipkart.com/rawpockets-graphic-print-men-s-round-neck-t-shirt/p/itme8qfa9zpwmzeg?pid=TSHE8QFA2YVHT8ER",
          "http://www.flipkart.com/sterling-rolling-pin-holder-tong-stainless-steel-kitchen-rack/p/itme9f9sg2r4qjj6?pid=KRKE9F9SRBFDZSPE",
          "http://www.flipkart.com/calibra-women-s-full-coverage-t-shirt-bra/p/itmeygh5ysz884ab?pid=BRAEYGH6GCHZQUJG",
          "http://www.flipkart.com/clovia-aqua-women-s-full-coverage-bra/p/itme87gyjt6ufycg?pid=BRAE6JCZAVVBXEFG",
          "http://www.flipkart.com/sg-vs-319-plus-kashmir-willow-cricket-bat/p/itmdcxvrzk4kdjhv?pid=BATDCXVFGC7BHGZK",
          "http://www.flipkart.com/sg-rsd-plus-kashmir-willow-cricket-bat/p/itmdczzzwtyddfkz?pid=BATDCG2BUYHJSUZE",
          "http://www.flipkart.com/baklol-printed-men-s-round-neck-t-shirt/p/itme8ggh99pd3rmn?pid=TSHE8GGHBFCQKMHV",
          "http://www.flipkart.com/huetrap-graphic-print-men-s-round-neck-t-shirt/p/itme8gf49wqnzyd4?pid=TSHE8GF4NWDCDSX2",
          "http://www.flipkart.com/huetrap-graphic-print-men-s-round-neck-t-shirt/p/itme8gf4b2hvkzkh?pid=TSHE8GF4NEEGKNRH",
          "http://www.flipkart.com/huetrap-graphic-print-men-s-round-neck-t-shirt/p/itme8gf4rxkmeerc?pid=TSHE8GF4ZQK2JVBS",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8z2zezenrzfz?pid=BRAE2XHUYWB7JYPR",
          "http://www.flipkart.com/sayitloud-printed-men-s-round-neck-t-shirt/p/itme3bwevafhj3e7?pid=TSHE3BWDKM9E2G46",
          "http://www.flipkart.com/deep-under-women-s-tube-bra/p/itmeytz49bwzu5zu?pid=BRAEYTZ4FSZ3FXSJ",
          "http://www.flipkart.com/avm-splash-20-20-kashmir-willow-cricket-bat/p/itmdtczymhabjxbq?pid=BATDF3AYH7YNCUZC",
          "http://www.flipkart.com/ss-ton-professional-english-willow-cricket-bat/p/itmdczzz23xa7zpn?pid=BATDCG2BN6HDVWPW",
          "http://www.flipkart.com/clovia-non-padded-wired-red-women-s-full-coverage-bra/p/itme8z2qfkgfycdg?pid=BRAE3HGCKX8PGBWH",
          "http://www.flipkart.com/ss-ton-heritage-english-willow-cricket-bat/p/itmdczzzybjwn5j9?pid=BATDCG2BY234294F",
          "http://www.flipkart.com/docare-trendy-women-s-full-coverage-bra/p/itme6tuc8fazefgm?pid=BRAE6TUC3XVE4ZTH",
          "http://www.flipkart.com/tab91-praveen-women-s-printed-top-pyjama-set/p/itme4sbxn8zfqwj9?pid=NSTE4SBXUUEFHGGV",
          "http://www.flipkart.com/john-players-men-s-checkered-formal-shirt/p/itme4magn88rdzkz?pid=SHTE4MAFFV6MM7HG",
          "http://www.flipkart.com/njoy-boy-s-kbp1-brief/p/itme9qy4bmndk7cz?pid=BRFE9QY4U9PZGVRH",
          "http://www.flipkart.com/bm-belmonte-ewc-toilet-seat-s-trap-western-commode/p/itmeefcxxysqjvt3?pid=CMDEEFCX8VGH3UYG",
          "http://www.flipkart.com/metmo-flip-flops/p/itmegwp9jtnrhdzp?pid=SFFEGWP99ZYHSHFM",
          "http://www.flipkart.com/i-voc-men-s-printed-casual-shirt/p/itme89zkhnnh525a?pid=SHTE89ZK8H5TTWTT",
          "http://www.flipkart.com/bleu-men-s-checkered-casual-shirt/p/itmey8unpmgs2n7a?pid=SHTEY8UNX8WYBSJG",
          "http://www.flipkart.com/chipchop-baby-girl-s-empire-waist-blue-dress/p/itmegq7x4mjbbrbc?pid=DREEJEYBGH53GSVF",
          "http://www.flipkart.com/kawachi-outdoor-sports-night-vision-driving-yellow-sunglass-plus-white-transparent-motorcycle-goggles/p/itme3h9mxmzzace7?pid=GOGE3H9MZYZEZFZV",
          "http://www.flipkart.com/tiny-toon-girl-s-gathered-red-dress/p/itme6tudaz7efztp?pid=DREE6TUDFCEGGVWM",
          "http://www.flipkart.com/quechua-forclaz-22-air-backpack/p/itme4dwqezpwtyf4?pid=SPBE4DWQDZWZDC7Q",
          "http://www.flipkart.com/outgear-domain/p/itmdt69vqbsayhek?pid=SPBDHUGSZWYGTS57",
          "http://www.flipkart.com/max-t-shirt/p/itmedmwxaxgw5q7e?pid=TSHEDMWXJYJCZQ9Y",
          "http://www.flipkart.com/wildcraft-waist-pouch/p/itmdeksz5jf9eyac?pid=SPBDEKSZ5JF9EYAC",
          "http://www.flipkart.com/wildcraft-digital-pouch-travel-bag/p/itmdt69wcvaw652a?pid=SPBDGGG8MYABNX6U",
          "http://www.flipkart.com/mount-track-discover-9107or-75-ltrs/p/itme3rjxc3uhce6b?pid=SPBE3RJXPR9DZTPT",
          "http://www.flipkart.com/coleman-rtx-3500i-c010-backpack/p/itmdt69w9nzs99kp?pid=SPBDHHHHXPZJDGYB",
          "http://www.flipkart.com/small-toes-slippers/p/itme7bg5ndsvytzh?pid=SFFE7BG5FK8KG25T",
          "http://www.flipkart.com/metmo-slippers/p/itmehgt4z7fxggcz?pid=SFFEHGT4TBH5ZTTJ",
          "http://www.flipkart.com/sai-senorita-solid-women-s-half-length-tights/p/itme9yq6ccvggatg?pid=TGTE9YQ6FSDDPPHE",
          "http://www.flipkart.com/varmora-vcst0-living-bedroom-stool/p/itmebkbzwjcpgcrv?pid=SLTEE6YYX9J6AYV5",
          "http://www.flipkart.com/favourite-bikerz-fbz-8784-112-db-vehicle-horn/p/itmea2yhqfm9avgn?pid=VHREA2YHV47FAKF5",
          "http://www.flipkart.com/destudio-tiny-wall-sticker/p/itmeyz5tzpmycyg5?pid=STIEYZ5TKK8CNADN",
          "http://www.flipkart.com/syska-led-lights-5-w-bulb/p/itme3z6xxfwfkezr?pid=BLBE3Z6XSRG54AQH",
          "http://www.flipkart.com/bling-book-case-ipad-2-3/p/itme2cezfhyqgznf?pid=ACCDCYB8NCGPEYEU",
          "http://www.flipkart.com/aps-sleeve-micromax-funbook-mini-p410/p/itmdxzk5e7z3pgnd?pid=ACCDXZK5X7SKPZZT",
          "http://www.flipkart.com/nike-casual-short-sleeve-printed-women-s-top/p/itme6ymhrpgemfsa?pid=TOPE6YMGKH2SZGMK",
          "http://www.flipkart.com/store-indya-hand-crafted-embossed-leather-diary-celtic-patterns-regular-journal-hard-bound/p/itme4bfnavqvwkag?pid=DIAE4BFMKWPXQF2M",
          "http://www.flipkart.com/jrs-fashion-women-s-leggings/p/itmey6d3gd6ctz4e?pid=LJGEY6D3VWCHKVPW",
          "http://www.flipkart.com/pepe-solid-v-neck-men-s-sweater/p/itmdzkygd6zfvmtr?pid=SWTDZKYDB5FJNPNJ",
          "http://www.flipkart.com/philips-12-5-w-led-stellar-bright-bulb/p/itmef3hez9vcyv3f?pid=BLBEF3HEDXF5EBVP",
          "http://www.flipkart.com/swarnim-jewellers-lord-ganesha-showpiece-7-5-cm/p/itme4zx42ggy8xhr?pid=SHIE4ZX45DEK8GY5",
          "http://www.flipkart.com/elan-a5-journal-ring-bound/p/itmdvyvstuhpcypz?pid=DIADSN4DSMJZWCPW",
          "http://www.flipkart.com/femninora-women-s-jeggings/p/itme7zc2rcz8mgwk?pid=LJGE7ZC2G7WRMNGY",
          "http://www.flipkart.com/designwallas-festive-pack-set-2-notebook-hard-bound/p/itmd4vtrtsm2f4yr?pid=DIAD4VTRTSM2F4YR",
          "http://www.flipkart.com/favourite-bikerz-fbz-6455-110-db-vehicle-horn/p/itmebsggem4fyzpb?pid=VHREBSGGGYMBXU5E",
          "http://www.flipkart.com/ornate-7-w-led-bulb/p/itmecsrfdypgjggf?pid=BLBECSRFVRR7XCZH",
          "http://www.flipkart.com/klick-women-s-leggings/p/itmdzjbctrettzws?pid=LJGDZJBCRTFHWPZM",
          "http://www.flipkart.com/favourite-bikerz-fbz-6480-110-db-vehicle-horn/p/itmebsmga2zuffty?pid=VHREBSMGYYUBVHHF",
          "http://www.flipkart.com/status-quo-solid-casual-men-s-sweater/p/itmdrchhk6wzfhdk?pid=SWTDRCHFRNTWNEEJ",
          "http://www.flipkart.com/peter-england-striped-round-neck-casual-men-s-sweater/p/itmea4akrj9w62vb?pid=SWTEA4AKGDGYDNAH",
          "http://www.flipkart.com/durian-bid-32625-a-2-leatherette-2-seater-sofa/p/itme9fs5k282kdbe?pid=SOFE9FS5ASZFGWVD",
          "http://www.flipkart.com/flora-casual-self-design-women-s-kurti/p/itme96acyrbwfnzq?pid=KRTEB48YQ2KV6CZE",
          "http://www.flipkart.com/hometown-ciaz-fabric-3-seater-sectional/p/itmeb7mhesja8yyz?pid=SOFEB7MHGWTHZFVJ",
          "http://www.flipkart.com/estyle-casual-festive-wedding-solid-women-s-kurti/p/itmeym23hgcyrh9z?pid=KRTEYM23GSPDWPKV",
          "http://www.flipkart.com/fab-rajasthan-unique-arts-casual-printed-women-s-kurti/p/itme8hqu94qzxzyp?pid=KRTE8HQUGTUCC8PX",
          "http://www.flipkart.com/quechua-solid-turtle-neck-casual-men-s-sweater/p/itme2mcebmb6vf2j?pid=SWTE2MCEV3ADGTAK",
          "http://www.flipkart.com/gmi-casual-solid-women-s-kurti/p/itme7rmrdn2egn7v?pid=KRTE7RMRRGYZSAET",
          "http://www.flipkart.com/durian-bid-32625-a-3-leatherette-3-seater-sofa/p/itme9fs5yf9yqqmt?pid=SOFE9FS5PGNNQV9N",
          "http://www.flipkart.com/takeincart-solid-baseball-cap/p/itme2zgg6dfyek7r?pid=CAPE2ZGGQ56T9HGZ",
          "http://www.flipkart.com/rubera-alloy-yellow-gold-bangle-set/p/itmeegmgmkeets8d?pid=BBAE52QH6R5GMSQA",
          "http://www.flipkart.com/urban-woods-white-women-heels/p/itmeegvmvjztaegy?pid=SNDE5PJGWDSXSDQN",
          "http://www.flipkart.com/voylla-alloy-zircon-yellow-gold-bangle-set/p/itme3qdnkfxbctc4?pid=BBAE3QDNUGVN8QYG",
          "http://www.flipkart.com/duke-striped-casual-men-s-sweater/p/itmdzchn7cveewry?pid=SWTDZCHNPYBTGZBX",
          "http://www.flipkart.com/estyle-casual-festive-wedding-printed-women-s-kurti/p/itme77xhcehn6rkh?pid=KRTE77XHSKPFQ9NY",
          "http://www.flipkart.com/life-shoppers-stop-geometric-print-v-neck-casual-men-s-reversible-sweater/p/itme7v5krg8krttz?pid=SWTE7V5K6JAMTFZQ",
          "http://www.flipkart.com/aadolf-women-heels/p/itme93upymbmkz5f?pid=SNDE93UPDQ5TNMZG",
          "http://www.flipkart.com/lotus-safe-sun-uv-screen-mattegel-spf-50-pa/p/itme53fvhzfgxm7f?pid=SNRE53FVTK2FQAKU",
          "http://www.flipkart.com/durian-clinton-a-3-leather-3-seater-sofa/p/itme94hw8zkgzput?pid=SOFE94HW8TPTGPNX",
          "http://www.flipkart.com/generix-book-cover-asus-fonepad-7-2014-fe170cg/p/itmebkbxpavdhgfh?pid=ACCEBKBXVFYQPJPZ",
          "http://www.flipkart.com/hunny-bunny-solid-girl-s-jumpsuit/p/itme8bzkaeswwsg6?pid=JUME8BZK5JR2KATK",
          "http://www.flipkart.com/estyle-casual-festive-polka-print-women-s-kurti/p/itmdxm88zwgf8ycs?pid=KRTDXM88AJFUVZWK",
          "http://www.flipkart.com/flora-solid-women-s-kurti/p/itme8wymgjhxz7hy?pid=KRTEE8SGZQWGZCUK",
          "http://www.flipkart.com/catwalk-women-heels/p/itme2cesmwmwyygz?pid=SNDDQYT6Y4FTMDDP",
          "http://www.flipkart.com/lotus-sun-block-cream-spf-30-pa/p/itme53fvmzag2yd9?pid=SNRE53FVWSRGRGS7",
          "http://www.flipkart.com/sebamed-multi-protect-sun-spray-spf-30-pa/p/itme3q38axxgfzba?pid=SNRE3Q384VRQC2ZP",
          "http://www.flipkart.com/just-herbs-sunnil-jojoba-grapeseed-moisturising-sun-protection-lotion-spf-30/p/itmdwtgq9tbyywgc?pid=SNRDWTGQ9FDKB33Y",
          "http://www.flipkart.com/eveready-14-w-led-bulb/p/itmeatuayfu4hqtz?pid=BLBEATUAUHNEQGTH",
          "http://www.flipkart.com/mocc-new-horn-set-imported-18-tunes-110-db-vehicle/p/itme8yhuwkhnszdu?pid=VHRE8YHUHAYGJZ2Y",
          "http://www.flipkart.com/jovees-anjeer-carrot-sunblock-pack-2-spf-45/p/itmdzhpqaa4ckkx8?pid=SNRDZHPMS2JSVHG5",
          "http://www.flipkart.com/takeincart-solid-baseball-cap/p/itme2zgggfvyekn7?pid=CAPE2ZGGBSYGHRWR",
          "http://www.flipkart.com/aveeno-baby-continuous-protection-lotion-sunscreen-broad-spectrum-spf-55-pa/p/itmdyyx99dfyxbfd?pid=SNRDZMQ862AJVKGG",
          "http://www.flipkart.com/catwalk-women-heels/p/itme2cepbyu6bhpa?pid=SNDE28TSTBZUGG8M",
          "http://www.flipkart.com/estyle-casual-festive-wedding-printed-women-s-kurti/p/itme4pxm2ayy8qjh?pid=KRTE4PXM3U9MTYPH",
          "http://www.flipkart.com/catwalk-women-heels/p/itme2cevhan2h4pw?pid=SNDE28TUKXHH5ZEW",
          "http://www.flipkart.com/aroma-magic-cucumber-sun-screen-lotion-2-spf-30-pa/p/itme56h4ehwhxgem?pid=SNRE56H4GFPNYGHV",
          "http://www.flipkart.com/lotus-herbals-safe-sun-matte-gel-spf-50-pa/p/itme5gp8gdn3ehnv?pid=SNRE5GP8YDRKNAKE",
          "http://www.flipkart.com/estyle-casual-festive-wedding-printed-women-s-kurti/p/itmeffgy8tuzgn9k?pid=KRTEFFGYSEQZEPCU",
          "http://www.flipkart.com/camy-alloy-metal-jewel-set/p/itme2v7fwb568mft?pid=JWSE2V7FY2EHVSZX",
          "http://www.flipkart.com/durian-berry-solid-wood-3-seater-sofa/p/itme8bzmumhqubyv?pid=SOFE8BZMFT7VRBSJ",
          "http://www.flipkart.com/catwalk-bellies/p/itme2cezhnmsuusa?pid=SHOE28TKBXVEFWZM",
          "http://www.flipkart.com/la-roche-posay-anthelios-xl-fluid-dry-touch-gel-cream-spf-50-pa/p/itmefchpgqhmgkpm?pid=SNREFCHPZR8YGBSX",
          "http://www.flipkart.com/infiniti-9-w-led-warm-white-b22-bulb/p/itmedmzy8zewpdab?pid=BLBEDMZYZSSCJUZH",
          "http://www.flipkart.com/catwalk-women-heels/p/itme2cemt4erevhh?pid=SNDE28TRKCZXHCJY",
          "http://www.flipkart.com/oshea-herbals-uvshield-sun-block-cream-spf-30-pa/p/itmeyghc694a5ezd?pid=SNREYGHCFWFGFA26",
          "http://www.flipkart.com/urban-woods-black-women-heels/p/itmeegvy9gde5z8z?pid=SNDE5PJGURDFBURG",
          "http://www.flipkart.com/eves-pret-porter-women-s-solid-casual-linen-shirt/p/itmeattu2dkmgzhb?pid=SHTEATTURTG7HX3X",
          "http://www.flipkart.com/naisha-women-s-printed-casual-shirt/p/itmecfpyr7zqar23?pid=SHTECFPYKSAGHGH2",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfyexwjvcbg?pid=SHTE4YFYJDWERKMR",
          "http://www.flipkart.com/karishma-women-s-solid-formal-shirt/p/itmdxynygs7ermfj?pid=SHTDXYNYZBPHFFFX",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itmeypeaegshqx3f?pid=SHTEYPEAG7JNSVNN",
          "http://www.flipkart.com/jazzy-ben-women-s-checkered-casual-shirt/p/itme94e9ztxknbhy?pid=SHTE94E9YHVD5YKW",
          "http://www.flipkart.com/blute-women-s-solid-casual-shirt/p/itme4zuysjdymwtq?pid=SHTE4ZUYKEZKHYJQ",
          "http://www.flipkart.com/vedika-jewellery-alloy-bangle-set/p/itme9zgyyjkhyhnx?pid=BBAE9ZGYGSUHMTXG",
          "http://www.flipkart.com/colors-couture-women-s-solid-casual-shirt/p/itmdzwny2tgajmkh?pid=SHTDZWNYY6D6H2CM",
          "http://www.flipkart.com/dede-s-women-s-solid-casual-shirt/p/itme4cnc6sgjsqee?pid=SHTE4CNCZVYKFS5Q",
          "http://www.flipkart.com/oxolloxo-women-s-printed-casual-shirt/p/itmeyx5hvude8pgs?pid=SHTEYX5H8NYSBBBW",
          "http://www.flipkart.com/identiti-women-s-printed-casual-shirt/p/itmefuhgrvyuyy7r?pid=SHTEFUHGAUHRCJ5J",
          "http://www.flipkart.com/pari-alloy-bangle-set/p/itmdwzfdh7pt4ydz?pid=BBADWZFDVJNFAMUH",
          "http://www.flipkart.com/mustard-women-s-solid-casual-shirt/p/itme38mzbu7yubwm?pid=SHTE38MZUZFNQQ5G",
          "http://www.flipkart.com/nexq-women-s-solid-casual-shirt/p/itmeb96cfvpwvqrw?pid=SHTEB96CYRMYSVZS",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpj2pzbajkf?pid=BBADVRPJYHHMUSFE",
          "http://www.flipkart.com/aussehen-women-s-solid-casual-shirt/p/itmefhf7t7gjdgfr?pid=SHTEFHF87D8XFUAE",
          "http://www.flipkart.com/bombay-high-women-s-floral-print-casual-shirt/p/itme3fcv3ewgfqzh?pid=SHTE3FCVRR7RXQ7W",
          "http://www.flipkart.com/karishma-women-s-solid-formal-shirt/p/itmdxpf5zjxybvnp?pid=SHTDXPF5YTCNDDDD",
          "http://www.flipkart.com/people-women-s-solid-casual-shirt/p/itmebtb9bgnmvp7d?pid=SHTEBTB9ZM42MVDY",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfystd5sqmz?pid=SHTE4YFY6PPGZNV6",
          "http://www.flipkart.com/karishma-women-s-printed-casual-shirt/p/itmdykjybhzfw89z?pid=SHTDYKJYN2HMCRFH",
          "http://www.flipkart.com/karishma-women-s-solid-casual-shirt/p/itmdzfvhysdmnckb?pid=SHTDZFVHY7TKGUMA",
          "http://www.flipkart.com/thegudlook-women-s-animal-print-casual-shirt/p/itmdxuzw2fdzyqx7?pid=SHTDXUZWDBXHW9WE",
          "http://www.flipkart.com/lee-cooper-women-s-printed-casual-shirt/p/itmdvhksyndgyhny?pid=SHTDVHKRK3SZAUB5",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfy6s6pknsh?pid=SHTE4YFYWCGZEPHB",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpj3ypkgdrh?pid=BBADVRPJZZZUASPZ",
          "http://www.flipkart.com/lee-cooper-women-s-checkered-casual-shirt/p/itmdvhkrrfzt9asa?pid=SHTDVHKQPDCXMJJ5",
          "http://www.flipkart.com/dressberry-women-s-solid-casual-shirt/p/itmey3btnepadrzq?pid=SHTEY3BTCJMHHVCN",
          "http://www.flipkart.com/life-shoppers-stop-women-s-solid-casual-shirt/p/itmeaz9pxszgfwmh?pid=SHTE6XPTSZWHHRD7",
          "http://www.flipkart.com/india-inc-women-s-solid-casual-shirt/p/itme9wh2zg46hjvz?pid=SHTE9WH3KDHUZYF6",
          "http://www.flipkart.com/meee-women-s-solid-casual-shirt/p/itme6wfr4ygznfrt?pid=SHTE6WFRGZJASZVJ",
          "http://www.flipkart.com/eves-pret-porter-women-s-solid-casual-shirt/p/itme9kp2nzvjn4bv?pid=SHTE9KP2HFAUNPPG",
          "http://www.flipkart.com/sukkhi-zinc-rhodium-bangle-set/p/itmdvrpj2b8tq785?pid=BBADVRPJZZNHWUGU",
          "http://www.flipkart.com/bombay-high-women-s-checkered-casual-shirt/p/itmdxpsxzyhzchnh?pid=SHTDXPSX8XZNNCZH",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itme4kbmbvaxeysa?pid=SHTE4KBM7NHQDAVA",
          "http://www.flipkart.com/cottinfab-women-s-checkered-casual-shirt/p/itmdzmbgfw8hkych?pid=SHTDZZHVJJJDEHQS",
          "http://www.flipkart.com/bedazzle-women-s-animal-print-casual-shirt/p/itme6j6g77h3zyhr?pid=SHTE6J6G6UCVVDHU",
          "http://www.flipkart.com/bombay-high-women-s-solid-formal-shirt/p/itmdua8cggf4thaa?pid=SHTDUA8CYNSGTQZF",
          "http://www.flipkart.com/mrigya-alloy-bangle-set/p/itme3zzvdxt2vvj3?pid=BBAE3ZZVU9G6XVNS",
          "http://www.flipkart.com/being-fab-women-s-checkered-casual-shirt/p/itme2zmytfxpgfrm?pid=SHTE2ZMYHPXDXUEH",
          "http://www.flipkart.com/blenni-women-s-solid-casual-shirt/p/itme83xzjcwdqgr8?pid=SHTE83XZYCAJEPJC",
          "http://www.flipkart.com/fast-n-fashion-women-s-checkered-casual-shirt/p/itmefwjh99ep7as6?pid=SHTEFWJHZWQ4RPYZ",
          "http://www.flipkart.com/sharani-yellow-gold-22-bangle/p/itme75harvfmuuav?pid=BBAE75HAMG45WNGF",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfyhfgynaae?pid=SHTE4YFYKYZZG4MN",
          "http://www.flipkart.com/meira-women-s-printed-party-shirt/p/itme2fct8mzcmrgh?pid=SHTE2FCTN7MYJCUW",
          "http://www.flipkart.com/wisstler-women-s-floral-print-casual-shirt/p/itme9wvrwkhfvzkg?pid=SHTE9WVSXWXXVN7A",
          "http://www.flipkart.com/camy-alloy-metal-18k-yellow-gold-bangle-set/p/itmeczbnggvzghkg?pid=BBAECZMBTFADPAHM",
          "http://www.flipkart.com/gmi-women-s-solid-casual-shirt/p/itme84eapyvfyt9e?pid=SHTE84EAUD62HGHE",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itmeyv3mucpnxjza?pid=SHTEYV3NHNXUVRGB",
          "http://www.flipkart.com/ishin-women-s-solid-party-shirt/p/itme3wvsxn4gvsym?pid=SHTE3WVSJMHBAKUA",
          "http://www.flipkart.com/orange-plum-women-s-floral-print-casual-shirt/p/itmebg8fkhhrcght?pid=SHTEBG8FZJFYB9DR",
          "http://www.flipkart.com/bombay-high-women-s-polka-print-formal-shirt/p/itme7f94haphgxcm?pid=SHTE7F94WHE65CJJ",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmefgbeajvgbhws?pid=BBAEFGBEZSSZGMFZ",
          "http://www.flipkart.com/being-fab-women-s-solid-casual-shirt/p/itme6gkkqazzk4cu?pid=SHTE6GKKTZ3MFZTH",
          "http://www.flipkart.com/eva-de-moda-women-s-graphic-print-casual-shirt/p/itme6pxk9xwncp3z?pid=SHTE6PXKYFE8Y3JT",
          "http://www.flipkart.com/fabpoppy-women-s-printed-casual-shirt/p/itme9szj2zvf44mg?pid=SHTE9SZJHUNFNVNG",
          "http://www.flipkart.com/lee-cooper-women-s-solid-casual-shirt/p/itmdyp6m3s5fkb3z?pid=SHTDYP6M8TXRF9U5",
          "http://www.flipkart.com/vanity-collection-women-s-solid-casual-shirt/p/itmeye95hsqzcpzc?pid=SHTEYE99AMMVKYDK",
          "http://www.flipkart.com/bombay-high-women-s-solid-casual-shirt/p/itmeye95ayhen5tf?pid=SHTEYE95VGBA4XXM",
          "http://www.flipkart.com/dede-s-women-s-solid-casual-shirt/p/itme4cncztqt7hev?pid=SHTE4CNCXQWEPQY9",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfykgcympsq?pid=SHTE4YFYME4TZPWK",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpjsmqnnptt?pid=BBADVRPJSSYQ9CG2",
          "http://www.flipkart.com/bombay-high-women-s-striped-formal-shirt/p/itmeye95gzmwjcgf?pid=SHTEYE998X2JFGDE",
          "http://www.flipkart.com/folklore-women-s-printed-festive-shirt/p/itme966p3uvaf26x?pid=SHTE966URDVWTHUZ",
          "http://www.flipkart.com/aimeon-women-s-solid-casual-shirt/p/itmebbwjfbbrjh5e?pid=SHTEBBWJXBH9GPHD",
          "http://www.flipkart.com/gmi-women-s-self-design-casual-shirt/p/itmeankus8agm24r?pid=SHTEANKUFFWHHJBU",
          "http://www.flipkart.com/cation-women-s-printed-casual-shirt/p/itme2me49eramdz2?pid=SHTE2ME4Y3QR83ZM",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itmeyuysdkug5huf?pid=SHTEYUYSXAEHDMTR",
          "http://www.flipkart.com/people-women-s-checkered-casual-shirt/p/itmea48rgnscuz8u?pid=SHTEA48RTJTHZY4Q",
          "http://www.flipkart.com/thegudlook-women-s-printed-casual-shirt/p/itmeyfc2stxyqgkx?pid=SHTEYFC2YNHHZX6H",
          "http://www.flipkart.com/lee-cooper-women-s-floral-print-casual-shirt/p/itmdyp6mnsrk6byj?pid=SHTDYP6MYFEVHQQ4",
          "http://www.flipkart.com/karishma-women-s-solid-formal-shirt/p/itmdxynyregx7n4u?pid=SHTDXYNYTHQHTPQY",
          "http://www.flipkart.com/pari-alloy-yellow-gold-bangle-set/p/itmdrupuem2ghtdu?pid=BBADRUPT2C7HVVS4",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme95rbnrkfmj87?pid=SHTE95RBF9JZMYSE",
          "http://www.flipkart.com/blute-women-s-solid-casual-shirt/p/itme4s4nr5mknquq?pid=SHTE4S4NH7GH6ZRH",
          "http://www.flipkart.com/kashana-fashions-women-s-printed-casual-shirt/p/itmea2g6ehhpnkfq?pid=SHTEARX7ZJDXFT8T",
          "http://www.flipkart.com/vedika-jewellery-alloy-bangle-set/p/itme9zgydbpvwqsh?pid=BBAE9ZGYTRBF75VW",
          "http://www.flipkart.com/cottinfab-women-s-solid-casual-shirt/p/itme37hpbfuhnysw?pid=SHTE37HP6HFZZAEE",
          "http://www.flipkart.com/dressberry-women-s-solid-casual-shirt/p/itme63xz5shfsdmx?pid=SHTE63XZJFHSSEQA",
          "http://www.flipkart.com/stylelite-women-s-solid-casual-formal-shirt/p/itmea8gtgghasa6y?pid=SHTEA8GTM6GGGEZB",
          "http://www.flipkart.com/life-shoppers-stop-women-s-printed-casual-formal-shirt/p/itme7ekpfgvzwpme?pid=SHTE6P4FWF9NHF3V",
          "http://www.flipkart.com/being-fab-women-s-striped-casual-shirt/p/itme2zmyurn54wkg?pid=SHTE2ZMZQVGQXCKG",
          "http://www.flipkart.com/rene-solid-women-s-kurti/p/itmecwcpcdmkdsak?pid=KRTECWCPVEBJ8J53",
          "http://www.flipkart.com/eves-pret-porter-women-s-printed-casual-shirt/p/itmeattugggams8d?pid=SHTEATTUXGYSFFM2",
          "http://www.flipkart.com/kashana-fashions-women-s-polka-print-casual-shirt/p/itmea2g6htyumfdw?pid=SHTEARX7G5EV5FJX",
          "http://www.flipkart.com/my-design-brass-alloy-yellow-gold-bangle-set/p/itme7qtpxpfxekxe?pid=BBAE7QTPGDJESHNS",
          "http://www.flipkart.com/bombay-high-women-s-checkered-casual-shirt/p/itmdxdm45yhjdzyy?pid=SHTDXDM4QZSFRCAT",
          "http://www.flipkart.com/bombay-high-women-s-striped-formal-shirt/p/itmeye958kghhwuj?pid=SHTEYE99ZFYA37JD",
          "http://www.flipkart.com/gmi-women-s-solid-casual-shirt/p/itme84eakazfqjnx?pid=SHTE84EA2BPH5FTY",
          "http://www.flipkart.com/hugo-chavez-women-s-solid-casual-denim-shirt/p/itme8cx8mravnfqq?pid=SHTE8CX8Q3SMVXSB",
          "http://www.flipkart.com/goodwill-impex-women-s-solid-casual-shirt/p/itme6yvvhkfkamwg?pid=SHTE6YVVZAUUCUKP",
          "http://www.flipkart.com/giftsnfriends-cotton-printed-dress-top-material/p/itme4kctphbjbphu?pid=FABE4KCTTX3UB4DT",
          "http://www.flipkart.com/giftsnfriends-cotton-printed-geometric-print-dress-top-material/p/itme4kctmy6zjbzk?pid=FABE4KCTDQPJUQSE",
          "http://www.flipkart.com/f-fashion-stylus-women-s-printed-casual-formal-shirt/p/itme6fwq65qrn6nw?pid=SHTE6FWQKBCFYAGX",
          "http://www.flipkart.com/stilestreet-women-s-solid-casual-shirt/p/itmdvy9yuftwhn7k?pid=SHTDW7AQUHWQUYHR",
          "http://www.flipkart.com/la-rochelle-women-s-geometric-print-casual-reversible-shirt/p/itme5y65f5gmhffy?pid=SHTE5Y655ACYCUAC",
          "http://www.flipkart.com/hermosear-women-s-solid-casual-shirt/p/itmdvc4gquppjmj3?pid=SHTDVC4GUEY3PZRC",
          "http://www.flipkart.com/ethnic-jewels-alloy-bangle-set/p/itme2znfgzbrq4gy?pid=BBAE3YT8EJ2S3PWA",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpjemtzzhyf?pid=BBADVRPJYKVBJH4Y",
          "http://www.flipkart.com/india-inc-women-s-solid-casual-shirt/p/itme8yzv5zjndxfj?pid=SHTE8YZWGRGDYEZQ",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itmeyuysj3ve6ape?pid=SHTEYUYSZGA5QYCM",
          "http://www.flipkart.com/luxor-alloy-yellow-gold-bangle-set/p/itme7yvpzpjrfdf9?pid=BBAE7YVPPEGDNGP4",
          "http://www.flipkart.com/tokyo-talkies-women-s-printed-casual-shirt/p/itme9794gkr5r6nu?pid=SHTE9795D6MYYRJ3",
          "http://www.flipkart.com/karishma-women-s-striped-formal-shirt/p/itmdzekgpcjhagxj?pid=SHTDZEKGZFZDVCKJ",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpja87cmyq6?pid=BBADVRPJUVEV7CPY",
          "http://www.flipkart.com/my-addiction-women-s-printed-casual-shirt/p/itmdsv7bzdhk9c9z?pid=SHTDSV7BZZWZDTWB",
          "http://www.flipkart.com/chic-unique-women-s-solid-party-shirt/p/itmefumgyyvgxuzg?pid=SHTEFUMGZHHHKKQZ",
          "http://www.flipkart.com/colors-couture-women-s-solid-party-shirt/p/itmdzwny4xz4cmgh?pid=SHTDZWNYZFV33BAX",
          "http://www.flipkart.com/bombay-high-women-s-solid-formal-shirt/p/itme29326hfwqxkj?pid=SHTE27TBBXZDJYRY",
          "http://www.flipkart.com/eves-pret-porter-women-s-floral-print-casual-shirt/p/itmeattuu5a4ghgs?pid=SHTEATTUPYGJ8FGG",
          "http://www.flipkart.com/picador-women-s-polka-print-casual-shirt/p/itmebeurwph5ewsn?pid=SHTEBEURERJVXNWR",
          "http://www.flipkart.com/dede-s-women-s-solid-casual-shirt/p/itme2hwgvqgfpqyu?pid=SHTE2HWGWBDXRFMH",
          "http://www.flipkart.com/lamora-women-s-checkered-casual-shirt/p/itme6k74gyrkgkf9?pid=SHTE6K74SNUAZWFS",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpjkmjausps?pid=BBADVRPJZYQ5MBZB",
          "http://www.flipkart.com/la-rochelle-women-s-geometric-print-casual-reversible-shirt/p/itme5y65f5gmhffy?pid=SHTE5Y65Q27B6XTS",
          "http://www.flipkart.com/eves-pret-porter-women-s-checkered-casual-shirt/p/itme76gk22v6m2hv?pid=SHTE76GKKAHACGYJ",
          "http://www.flipkart.com/chic-unique-women-s-solid-party-shirt/p/itmefumgzhhyjahd?pid=SHTEFUMGZHQXWA4M",
          "http://www.flipkart.com/sukkhi-alloy-yellow-gold-bangle-set/p/itme7f9bhd7dy8en?pid=BBAE7F9BHY3SSBGM",
          "http://www.flipkart.com/my-addiction-women-s-printed-casual-shirt/p/itmdsv7baqtqj4nz?pid=SHTDSV7BZ9YSXYY3",
          "http://www.flipkart.com/karishma-women-s-printed-casual-shirt/p/itmdykjykhwtufmg?pid=SHTDYKJYKZKGZS9T",
          "http://www.flipkart.com/ethnic-jewels-alloy-yellow-gold-bangle-set/p/itme7agxkhgbsngq?pid=BBAE7AGX9CTCWX3W",
          "http://www.flipkart.com/karishma-women-s-printed-casual-shirt/p/itmdykjygcztbkzc?pid=SHTDYKJYRSAJVHQH",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme95rb33rsbcgc?pid=SHTE95RBGBFDKVZF",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itmeyv3mh2dfwfdc?pid=SHTEYV3NX7CCHPME",
          "http://www.flipkart.com/vedika-jewellery-alloy-bangle-set/p/itme9zgydp3vjsez?pid=BBAE9ZGYZGFMTBUZ",
          "http://www.flipkart.com/being-fab-women-s-striped-casual-shirt/p/itme2zmyzkmqgcnt?pid=SHTE2ZMZJFVWXJ5M",
          "http://www.flipkart.com/bombay-high-women-s-solid-formal-shirt/p/itme7f94zcabss2k?pid=SHTE7F94BCBVQFHH",
          "http://www.flipkart.com/meee-women-s-solid-casual-shirt/p/itme8gcdphn2dqqr?pid=SHTE8GCDEMKSUYHQ",
          "http://www.flipkart.com/dede-s-women-s-printed-casual-shirt/p/itme55hgsyc3gzyc?pid=SHTE55HGUD8ESUTQ",
          "http://www.flipkart.com/bombay-high-women-s-solid-casual-shirt/p/itmdxdm4sfhfhkjf?pid=SHTDXDM4QY59UHZR",
          "http://www.flipkart.com/dede-s-women-s-solid-casual-shirt/p/itme4cndqzdj9mxf?pid=SHTE4CNCEMRZVBEH",
          "http://www.flipkart.com/aardee-women-s-printed-casual-shirt/p/itme6z7atznwveam?pid=SHTE6Z7AHX8VZSGS",
          "http://www.flipkart.com/karishma-women-s-printed-casual-shirt/p/itmdykjyhfuaspsa?pid=SHTDYKJYZWJQEJK9",
          "http://www.flipkart.com/adhaans-women-s-printed-casual-shirt/p/itme8h95rqqat2w3?pid=SHTE8H95ZHYJ9TCW",
          "http://www.flipkart.com/lee-cooper-women-s-checkered-casual-shirt/p/itmdvhkrh7edsg3z?pid=SHTDVHKPPMUFYH6D",
          "http://www.flipkart.com/karishma-women-s-solid-formal-shirt/p/itmdxxkft2hj2by7?pid=SHTDXXKFYPQ4ANVV",
          "http://www.flipkart.com/my-addiction-women-s-printed-casual-shirt/p/itmdtyyp8rguwypa?pid=SHTDTYYPSUZGKH89",
          "http://www.flipkart.com/kiosha-women-s-printed-casual-shirt/p/itme8bfqh9nhjgyh?pid=SHTE8BFQRV6SDRP6",
          "http://www.flipkart.com/dressberry-women-s-solid-casual-shirt/p/itme5efy9swbrzhg?pid=SHTE5EFYW3HTFZGV",
          "http://www.flipkart.com/bombay-high-women-s-striped-formal-shirt/p/itmdxgkk5mbeupaw?pid=SHTDXGKKYNYSGKKK",
          "http://www.flipkart.com/dressberry-women-s-solid-casual-shirt/p/itmey3bt4esyryen?pid=SHTEY3BTTRDEXAGT",
          "http://www.flipkart.com/bedazzle-women-s-checkered-casual-shirt/p/itmefevcdgyg4nkp?pid=SHTEFEVDJKHMCFRC",
          "http://www.flipkart.com/lee-cooper-women-s-checkered-casual-shirt/p/itmdzjfwu7y8fzgk?pid=SHTDZJFVVAGGZCCW",
          "http://www.flipkart.com/bombay-high-women-s-striped-casual-shirt/p/itmdua8chjbdvdrv?pid=SHTDUA8CYBFUN4PU",
          "http://www.flipkart.com/being-fab-women-s-checkered-casual-shirt/p/itmeyyy4rfwg84hu?pid=SHTEYYY4N2GNKWXH",
          "http://www.flipkart.com/karishma-women-s-striped-formal-shirt/p/itmdzekgnsnfy6zz?pid=SHTDZEKGW6AZV9CY",
          "http://www.flipkart.com/blute-women-s-striped-casual-shirt/p/itme4t6fhpb8ebge?pid=SHTE4T6FGDXABBHN",
          "http://www.flipkart.com/solah-shringar-lac-bangle-set/p/itmecvgwemd92fr3?pid=BBAECVGX7ZKEM3UC",
          "http://www.flipkart.com/jazzy-ben-women-s-checkered-casual-shirt/p/itme8c98yzfzkptf?pid=SHTE8C98PYTHAZ5T",
          "http://www.flipkart.com/concepts-women-s-embroidered-casual-denim-shirt/p/itme8gvyugygaeej?pid=SHTE8GVYNAJKT5HY",
          "http://www.flipkart.com/dapinc-acrylic-bangle-set/p/itmecb8fbwyx3gqp?pid=BBAECB8FBGJUWWH4",
          "http://www.flipkart.com/jazzup-women-s-striped-casual-shirt/p/itme2gyxug7xpgbv?pid=SHTE2GYXNYYWW459",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itmdvrpjfw43b85p?pid=BBADVRPJUC3RU7F3",
          "http://www.flipkart.com/bombay-high-women-s-solid-formal-shirt/p/itmdua8cbgpgszy9?pid=SHTDUA8DXHWKTUVD",
          "http://www.flipkart.com/anouk-women-s-printed-casual-shirt/p/itme4nr3gxuzsqvk?pid=SHTE4NR3HFWFBDUW",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme955nnfhmab7a?pid=SHTE95RB9NPYAC8R",
          "http://www.flipkart.com/sukkhi-copper-yellow-gold-bangle-set/p/itme7f9bd8ephmgm?pid=BBAE7F9BB6ZSZZTU",
          "http://www.flipkart.com/miss-rich-women-s-solid-casual-shirt/p/itme4yfyq8bmzvak?pid=SHTE4YFYH2VVWTBJ",
          "http://www.flipkart.com/modimania-women-s-self-design-casual-formal-festive-party-shirt/p/itme7p7xu6rdp7rt?pid=SHTE7P7XSYGKYGAX",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme955nnfhmab7a?pid=SHTE95RBYGWYGDVY",
          "http://www.flipkart.com/kashana-fashions-women-s-printed-casual-shirt/p/itmea2g647y54ymh?pid=SHTEAGWVSH5NSBZP",
          "http://www.flipkart.com/kashana-fashions-women-s-polka-print-casual-shirt/p/itmed6ghbzxcbyz4?pid=SHTEANHWKH5AJVFG",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme95rbz3zbyuc7?pid=SHTE95RB6PQEEFDN",
          "http://www.flipkart.com/mrigya-alloy-metal-bangle-set/p/itmdye6hzrtxjvf3?pid=BBADYE6HFZKJD6FG",
          "http://www.flipkart.com/femninora-women-s-solid-casual-formal-shirt/p/itme95rbswamynzf?pid=SHTE95RCVYGEY4YS",
          "http://www.flipkart.com/fashion-fusion-alloy-yellow-gold-bangle-set/p/itme3fsuyf52tff4?pid=BBAE3FSU8BZS8VHT",
          "http://www.flipkart.com/hermosear-women-s-solid-casual-shirt/p/itmdvc4gw3aghyhu?pid=SHTDVC4GXFZM7WGR",
          "http://www.flipkart.com/karishma-women-s-solid-formal-shirt/p/itmdxxkfxqxjgbsr?pid=SHTDXXKFVY8FCKJN",
          "http://www.flipkart.com/bombay-high-women-s-checkered-formal-shirt/p/itme7f94fs6wbfug?pid=SHTE7F94FNDKCBQV",
          "http://www.flipkart.com/camy-alloy-brass-bangle-set/p/itme4hbe2xgm8mmq?pid=BBAE4HBESXXHACEM",
          "http://www.flipkart.com/osumfab-women-s-solid-casual-formal-shirt/p/itme6y4677zgnfrg?pid=SHTE6Y46VSVGNZ4K",
          "http://www.flipkart.com/vedika-jewellery-alloy-bangle-set/p/itme9zgydp3vjsez?pid=BBAE9ZGYVSGPHHKM",
          "http://www.flipkart.com/desigrrrl-women-s-floral-print-casual-shirt/p/itme5j3795fa7gga?pid=SHTE5J37G5NZEACS",
          "http://www.flipkart.com/india-inc-women-s-floral-print-casual-shirt/p/itmeap5yhbfyafdn?pid=SHTEAP5YP4TNNNHE",
          "http://www.flipkart.com/kashana-fashions-women-s-solid-casual-shirt/p/itme7vfkvgpkgg92?pid=SHTE7VFKXCYHZY5C",
          "http://www.flipkart.com/am-you-women-s-printed-casual-shirt/p/itmdxpseswpygwum?pid=SHTDXPSEJQCAZGE4",
          "http://www.flipkart.com/nexq-women-s-solid-casual-shirt/p/itmeb96cguz6vm4e?pid=SHTEB96CPNPNXS3H",
          "http://www.flipkart.com/pari-brass-bangle-set/p/itmdrupuc9vtn4d7?pid=BBADRUPT8RG6KZAH",
          "http://www.flipkart.com/ethnic-jewels-alloy-yellow-gold-bangle-set/p/itme7agxdvkghtdy?pid=BBAE7AGXF7XM42G6",
          "http://www.flipkart.com/duvi-women-s-floral-print-casual-shirt/p/itme8wqtqrn4yvxr?pid=SHTE8WQTQFFMHMGM",
          "http://www.flipkart.com/being-fab-women-s-checkered-casual-shirt/p/itmey2z4zwebrmbt?pid=SHTEY2Z4ZZYHB7GZ",
          "http://www.flipkart.com/alibi-inmark-women-s-solid-casual-shirt/p/itmeb72xmwbkgjcw?pid=SHTE8E6YZH27RHZG",
          "http://www.flipkart.com/kiosha-women-s-checkered-casual-shirt/p/itme8bfqk36pc6cx?pid=SHTE8BFQZAZFMKJG",
          "http://www.flipkart.com/united-bags-density-35-l-medium-laptop-backpack/p/itmeegdnrcfkbghz?pid=BKPEYQHB6J2PN9R4",
          "http://www.flipkart.com/aviiq-book-cover-apple-ipad-mini/p/itme5daa2aakzcne?pid=ACCE5DAAJGHATWZA",
          "http://www.flipkart.com/adraxx-remote-control-realstic-sedan-toy-car/p/itmdwtg6udeyf34y?pid=RCTDWTG6YVYEMHEA",
          "http://www.flipkart.com/jaipur-crafts-premium-collection-silver-lord-krishna-makhan-matki-showpiece-13-97-cm/p/itmecznmyddxf9b4?pid=SHIECZNMYRAQJHRW",
          "http://www.flipkart.com/as42-floral-print-women-s-regular-skirt/p/itmeadmf6gutqgzy?pid=SKIEADMF6MEE9PWU",
          "http://www.flipkart.com/syma-x5-quadcopter/p/itme6bq43ycz5ehr?pid=RCTE6BQ4BK8XQQKF",
          "http://www.flipkart.com/bendly-outrider-rucksack-60-l/p/itme8jzacatd6dgd?pid=RKSE8JZAPUG4AK3F",
          "http://www.flipkart.com/ratnam-gold-diamond-18-k-ring/p/itme3hstcjwnwgny?pid=RNGE3HSTTP6C9ASW",
          "http://www.flipkart.com/dressberry-solid-women-s-wrap-around-skirt/p/itme45x35umfnkx2?pid=SKIE45X3FZDSF4BK",
          "http://www.flipkart.com/estrella-companero-pamplona-30-l-backpack/p/itme79uxmz7hyjna?pid=BKPE79UX3AHF8JQR",
          "http://www.flipkart.com/zero-gravity-fearless-7109-40-l-rucksack/p/itme7fr5zag5phk7?pid=SPBE7FR5SM8SPZTD",
          "http://www.flipkart.com/united-bags-bundi-tt-35-l-laptop-backpack/p/itme6np9rvhsfvhc?pid=BKPE6NP9CNQSFSFQ",
          "http://www.flipkart.com/aviiq-book-cover-apple-ipad-mini/p/itme5dfuhgwtegq3?pid=ACCE5DFUEN7HYYHZ",
          "http://www.flipkart.com/nikko-vaporizr/p/itmdhpzxpyytp4zf?pid=RCTDHPZTWCHTKKSW",
          "http://www.flipkart.com/x-doria-back-cover-ipad-2/p/itmdcmmpq9vcwegh?pid=ACCDCMMNZWMACPQW",
          "http://www.flipkart.com/philips-qg3383-7-in-1-multigrooming-pro/p/itmdkayxdprdqbyy?pid=SHVDKAYXPNNHWZAD",
          "http://www.flipkart.com/lavie-chic-4-backpack/p/itme3zdhrfgnzbpd?pid=BKPE3Z2HBCVZZZGR",
          "http://www.flipkart.com/remington-hair-clipper-hc5810-genius-trimmer-men/p/itmd2h86kmvv9jvg?pid=SHVD2H7URCYYAHAH",
          "http://www.flipkart.com/rock-polo-5204-laptop-backpack/p/itmey9tncvkn68e6?pid=BKPEY9TNHRGN9HRM",
          "http://www.flipkart.com/silverlit-sky-dagger/p/itmdwr8fzjrgshpb?pid=RCTDWR8FFE5FCH5H",
          "http://www.flipkart.com/shivani-art-jesus-sheep-plate-showpiece-18-cm/p/itme7kdvubyak2yj?pid=SHIE7KDV9H9YEHZ6",
          "http://www.flipkart.com/kolorfish-flip-cover-apple-ipad-2-3-4/p/itmefzvev3gth2mt?pid=ACCEFZVEKCR9BQJQ",
          "http://www.flipkart.com/united-bags-camouflage-35-l-medium-laptop-backpack/p/itmeegdnszd2k9ge?pid=BKPEFKJYGPRQWMZ7",
          "http://www.flipkart.com/rock-book-cover-ipad-mini/p/itmdmwehw77uhpzn?pid=ACCDMWEGPQXZUTYZ",
          "http://www.flipkart.com/airplus-book-cover-ipad-air/p/itmdsb6edatn75uh?pid=ACCDSB6EJXB8B9GG",
          "http://www.flipkart.com/story-home-checkered-double-dohar-white/p/itme2hwcavygkugg?pid=BLAE2HWCGMSQV2F5",
          "http://www.flipkart.com/northwear-scholor-2-l-big-backpack/p/itme4mu4xkenxyhh?pid=BKPE4MU4T2CJ5YTJ",
          "http://www.flipkart.com/coddle-pocket-cloth-diaper-plus-microfiber-insert/p/itmedku4txsqhqgc?pid=NPYEDKU4ZQ2KTE3W",
          "http://www.flipkart.com/prism-sky-king-four-axis-aircraft-2-4g-rc-x39/p/itme38hxdz8m49hz?pid=RCTE38HXGH4CJEPH",
          "http://www.flipkart.com/wilson-championship-extra-duty-tennis-ball/p/itmdcjffgzhqndt6?pid=BALDCJFFGZHQNDT6",
          "http://www.flipkart.com/rock-flip-cover-apple-ipad-mini-retina/p/itmdrsjsghs9xrgz?pid=ACCDRSJR2EEPBYUG",
          "http://www.flipkart.com/zwart-gurner-25-l-medium-laptop-backpack/p/itmeefbuxm2vnz75?pid=BKPEAM9EGPND2SNG",
          "http://www.flipkart.com/remington-body-hair-bht6100-trimmer-men/p/itmd8jf3ntwffsvw?pid=SHVD8JYZHHVHBA6V",
          "http://www.flipkart.com/president-pyramid/p/itmdwg6ggwwcugdj?pid=SPBDWG6GJGTSWQVT",
          "http://www.flipkart.com/rock-book-cover-samsung-galaxy-note-8-0-n5100/p/itmdhhwgrebfudxb?pid=ACCDHHWFSWVWGXDY",
          "http://www.flipkart.com/rock-flip-cover-ipad-air/p/itmds2gzahfxm9mu?pid=ACCDS2HWGTMJGVHP",
          "http://www.flipkart.com/ratnam-gold-diamond-18-k-ring/p/itme3jrmccsgjtce?pid=RNGE3JRMHKFGFEXH",
          "http://www.flipkart.com/folklore-solid-women-s-a-line-skirt/p/itmea8sscdhgsshr?pid=SKIEA8SSSEUAQ8CW",
          "http://www.flipkart.com/hoa-baby-nappy-set-6-plain-pure-cotton-assorted/p/itme5quh8cf6tcvf?pid=NPYE5QUHW3Y8TGMY",
          "http://www.flipkart.com/rock-flip-cover-tab-s-8-4/p/itmdyhszq5znmtgz?pid=ACCDYHSZ8YYYY7C3",
          "http://www.flipkart.com/xq-chevrolet-camaro/p/itmdbtjckfgfcfgf?pid=RCTDBTJ6ZHJ3H2XF",
          "http://www.flipkart.com/kemei-body-groomer-km-30005-trimmer-men/p/itme5kz9rgpzm9gs?pid=SHVE5KZ9ZWJKGCHH",
          "http://www.flipkart.com/capdase-flip-cover-apple-ipad-mini-retina-display/p/itmdtd3frbbcmeyc?pid=ACCDTD2ZVUHW6HZA",
          "http://www.flipkart.com/united-bags-g-checks-35-l-medium-laptop-backpack/p/itmeegdnmgrudcdg?pid=BKPE497YU7UDFWYQ",
          "http://www.flipkart.com/dicapac-grip-back-cover-galaxy-note/p/itmdswhx2ggepzya?pid=ACCDSWHWFDAK95ZT",
          "http://www.flipkart.com/dhrohar-red-72-cm-table-runner/p/itme4whjxzzgygke?pid=TBRE4WHJJCNFH4FT",
          "http://www.flipkart.com/foolzy-pack-24-lipsticks-84-g/p/itmebjhxyqthagdv?pid=LSKEBQ8T4BJMATMX",
          "http://www.flipkart.com/maybelline-super-stay-14-hr-lipstick-coral-craze-nail-enamel-3-3-g/p/itme9cgxhrjpevb6?pid=LSKE9CGXRCJ7JHFF",
          "http://www.flipkart.com/canon-toner-cartridge-416-black/p/itmdyvctd68aaxsf?pid=INKDYVCRYMNQAZKR",
          "http://www.flipkart.com/styletoss-full-sleeve-solid-women-s-sweatshirt/p/itme37hhuh7cjbrw?pid=SWSE37HH2F2M25CH",
          "http://www.flipkart.com/wrangler-printed-men-s-round-neck-t-shirt/p/itmdshqffz2ftzhs?pid=TSHDSHQEKAECUYFH",
          "http://www.flipkart.com/white-kalia-graphic-print-men-s-round-neck-t-shirt/p/itmdx5n6zzfgu6yf?pid=TSHDX5N6ZEEWFNG2",
          "http://www.flipkart.com/well-embroidered-men-s-polo-neck-t-shirt/p/itmecav5y4t5erhy?pid=TSHECAV5C2HN5GY7",
          "http://www.flipkart.com/wrangler-solid-men-s-v-neck-t-shirt/p/itmdxwed6xdargc5?pid=TSHDXWECXZ5HWJCA",
          "http://www.flipkart.com/wrogn-solid-men-s-v-neck-t-shirt/p/itme5neeh2pr53yz?pid=TSHE5NEEUSZNTU2J",
          "http://www.flipkart.com/esteem-boy-s-drawer/p/itmefzgzefzga3az?pid=BLREFZGP3QCZZZTG",
          "http://www.flipkart.com/stylofashiongarments-slim-fit-women-s-jeans/p/itmehka3vuavhukg?pid=JEAEHKA3F4REG4SJ",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kbgkazmhufb?pid=TSHE6KBGGWZQGZDZ",
          "http://www.flipkart.com/numero-uno-printed-men-s-round-neck-t-shirt/p/itme5vvp6ra4nayf?pid=TSHE5VVMQ4FPZVZJ",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itme7h2d6wqzav7d?pid=TSHE7H2DQYMGCHJZ",
          "http://www.flipkart.com/ninja-turtles-printed-men-s-round-neck-t-shirt/p/itmef3z3dunr5yng?pid=TSHEF3Z3ASHT3HN7",
          "http://www.flipkart.com/ninja-turtle-printed-men-s-polo-t-shirt/p/itmefjfzrnyjw6p7?pid=TSHEFJFZCGXRYC9X",
          "http://www.flipkart.com/numero-uno-printed-men-s-v-neck-t-shirt/p/itme5nyhqgfecxzj?pid=TSHE5NYHTEWHGM6B",
          "http://www.flipkart.com/nivia-solid-men-s-round-neck-t-shirt/p/itme4yhuz9fzxk4a?pid=TSHE4YJMPHQXTPZZ",
          "http://www.flipkart.com/ocean-race-solid-men-s-round-neck-t-shirt/p/itme93rzrgdqaatk?pid=TSHE93RYGKYFFBHA",
          "http://www.flipkart.com/orange-orchid-striped-men-s-polo-t-shirt/p/itme2mevpkgwm9c8?pid=TSHE2MEWQHFHRAN8",
          "http://www.flipkart.com/nucode-striped-men-s-polo-neck-t-shirt/p/itmea7w9qzcrhz5c?pid=TSHEA7W9NV6FMEZ5",
          "http://www.flipkart.com/nod-r-solid-men-s-round-neck-t-shirt/p/itmecvf5wzgxehhv?pid=TSHECVF5ZH6E4KFQ",
          "http://www.flipkart.com/ninja-turtles-printed-men-s-round-neck-t-shirt/p/itmef3z3dunr5yng?pid=TSHEF3Z3ZMGUWF6P",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itmea7w98cjygwjj?pid=TSHEA7W9E9WHVBTM",
          "http://www.flipkart.com/omtex-solid-men-s-polo-neck-t-shirt/p/itmedhnggwqytpap?pid=TSHE7FR6UX9YJTBE",
          "http://www.flipkart.com/nucode-solid-men-s-polo-neck-t-shirt/p/itme5hqfcbgyjae2?pid=TSHE5HQFW3MXDYKV",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itmdz5p2uct8hymf?pid=TSHDZ5ZJUNTXSZK8",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwdw8zhtedn?pid=TSHE6KWDUJHUJ2DD",
          "http://www.flipkart.com/nucode-solid-men-s-polo-neck-t-shirt/p/itme5hqfdycpmcej?pid=TSHE5HQFQ6FXP9GY",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwduwcykguv?pid=TSHE6KWDZ7RES3RA",
          "http://www.flipkart.com/numero-uno-striped-men-s-v-neck-t-shirt/p/itme5vvztjqthgxh?pid=TSHE5VVMYGFWVNRF",
          "http://www.flipkart.com/nimya-solid-men-s-polo-neck-t-shirt/p/itme66chyb5j7f6r?pid=TSHE66CHHB7WYRVE",
          "http://www.flipkart.com/nitlon-solid-men-s-round-neck-t-shirt/p/itme9cggrrvgyxv7?pid=TSHE9CGGGVYT3KR8",
          "http://www.flipkart.com/ninja-turtle-printed-men-s-round-neck-t-shirt/p/itmdz6s34yvjkgcy?pid=TSHDZ6S2CJPBHZGK",
          "http://www.flipkart.com/numero-uno-solid-men-s-v-neck-t-shirt/p/itmebuz7jkjkzdqx?pid=TSHEBUZ7DHB8XBHV",
          "http://www.flipkart.com/ocean-race-graphic-print-men-s-round-neck-t-shirt/p/itme9k9gygyafyts?pid=TSHE9K9JEJBYHQQF",
          "http://www.flipkart.com/nucode-striped-men-s-polo-neck-t-shirt/p/itmea7w9f6zz5jtq?pid=TSHEA7W9HFSF5J9Y",
          "http://www.flipkart.com/orange-orchid-striped-men-s-polo-t-shirt/p/itme2mesk7nymt6y?pid=TSHE2MEYYYQBTBEY",
          "http://www.flipkart.com/ocean-9-solid-men-s-polo-t-shirt/p/itmdzczyxkegdmef?pid=TSHDZCZYMDX6BKQD",
          "http://www.flipkart.com/ocean-9-solid-men-s-fashion-neck-t-shirt/p/itmdzczyrkgsnr45?pid=TSHDZCZYMDZHRBFK",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kbgwfzygmxk?pid=TSHE6KBGSBZKED4U",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itmedhtj4hkwphv2?pid=TSHE7KBHSZGHUHHE",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itme7kbhycthzzgf?pid=TSHE7KBM54F2ZQBF",
          "http://www.flipkart.com/nucode-graphic-print-men-s-v-neck-t-shirt/p/itme6kwcfdgdgw88?pid=TSHE6KWCHQSQAKK4",
          "http://www.flipkart.com/ninja-turtle-printed-men-s-round-neck-t-shirt/p/itmdz6s33mgvdunj?pid=TSHDZ6S2QPKKYVSF",
          "http://www.flipkart.com/ninja-turtle-printed-men-s-round-neck-t-shirt/p/itmefjfznyzc6efy?pid=TSHEFJFZVADWKUVC",
          "http://www.flipkart.com/orange-orchid-printed-men-s-round-neck-t-shirt/p/itme3fcughw5wpne?pid=TSHE3FCUPNHUYZWY",
          "http://www.flipkart.com/ninja-turtle-printed-men-s-round-neck-t-shirt/p/itmdz6s3zjvaeewq?pid=TSHDZ6S2XWQUHWZ9",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itmdz5p2dhre3f7v?pid=TSHDZ5ZJTQR6WBY8",
          "http://www.flipkart.com/okane-self-design-men-s-polo-neck-t-shirt/p/itme3eyc9jrf42zc?pid=TSHE3EYCXNMCM9NN",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itme7kbmzsnva2gm?pid=TSHE7KBMVFRKXA6N",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kbgb2k9zhvy?pid=TSHE6KBGSTNZHJHP",
          "http://www.flipkart.com/nitlon-solid-men-s-round-neck-t-shirt/p/itme9cgge9gssrtd?pid=TSHE9CGGP6VHNMZ5",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itmdvn8wsffwyut2?pid=TSHDVN8WRWGY4QZN",
          "http://www.flipkart.com/nucode-striped-men-s-polo-neck-t-shirt/p/itmea7w9qzcrhz5c?pid=TSHEA7W9VCKX2DSJ",
          "http://www.flipkart.com/nuteez-printed-men-s-round-neck-t-shirt/p/itmdttqf2jg9wekg?pid=TSHDTTQFSGZUTURG",
          "http://www.flipkart.com/orange-orchid-solid-printed-men-s-round-neck-t-shirt/p/itme2nmj7t7bqdsg?pid=TSHE2NMKT88GYMGH",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwd7hfdjz8q?pid=TSHE6KWDSPNRHFDC",
          "http://www.flipkart.com/nucode-geometric-print-men-s-round-neck-t-shirt/p/itme6kwdfmztgrkb?pid=TSHE6KWDYXYAYTZM",
          "http://www.flipkart.com/numero-uno-printed-men-s-polo-neck-t-shirt/p/itme5nyhxxhftcdx?pid=TSHE5NYHZY8JZDDF",
          "http://www.flipkart.com/nivia-solid-men-s-round-neck-t-shirt/p/itme4yhuc3ftzmqg?pid=TSHE4YJMZHNXAG4C",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwd6buhetup?pid=TSHE6KWDZSGWYGAF",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwdzmdmywb7?pid=TSHE6KWDZRGJHNYA",
          "http://www.flipkart.com/orange-orchid-printed-men-s-round-neck-t-shirt/p/itme2meszhdehcwe?pid=TSHE2MESF3ATPA7G",
          "http://www.flipkart.com/o-printed-men-s-round-neck-t-shirt/p/itme3h9tsq6ttnau?pid=TSHE3H9TZJNYMHUW",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itme5vvppkphj9cz?pid=TSHE5VVMMGZC7Z2T",
          "http://www.flipkart.com/numero-uno-solid-men-s-v-neck-t-shirt/p/itmdz5p2jzfqfjvn?pid=TSHDZ5ZJZGF75KGA",
          "http://www.flipkart.com/omtex-solid-men-s-polo-neck-t-shirt/p/itmedhnggwqytpap?pid=TSHE7FR6QVBUM7KM",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itmdz5p2uct8hymf?pid=TSHDZ5ZJ4Q7KGCDN",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itme7kbmz4uwpczr?pid=TSHE7KBH5J56JY4F",
          "http://www.flipkart.com/ovl-graphic-print-men-s-round-neck-t-shirt/p/itme7kbh9dhkuwft?pid=TSHE7KBH65QU5PJE",
          "http://www.flipkart.com/nucode-striped-men-s-polo-neck-t-shirt/p/itmea7w9ty5fdhcn?pid=TSHEA7W92TPXC6JH",
          "http://www.flipkart.com/numero-uno-striped-men-s-polo-t-shirt/p/itmdz5p2dhre3f7v?pid=TSHDZ5ZJ3QDK8ZNB",
          "http://www.flipkart.com/orange-orchid-solid-men-s-round-neck-t-shirt/p/itme2rx8hgxbq3hf?pid=TSHE2RX9HZRG32QQ",
          "http://www.flipkart.com/orange-orchid-printed-men-s-round-neck-t-shirt/p/itme2meszhdehcwe?pid=TSHE2MFFGPTJK4PH",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwdygrgn22x?pid=TSHE6KWDZZTPGFMG",
          "http://www.flipkart.com/nucode-graphic-print-men-s-round-neck-t-shirt/p/itme6kwdbhtzacyk?pid=TSHE6KWDZJCPGGEZ",
          "http://www.flipkart.com/ocean-race-graphic-print-men-s-round-neck-t-shirt/p/itme9kfp4g4jtfy4?pid=TSHE9KFZHUFGPHJE",
          "http://www.flipkart.com/ocean-race-solid-men-s-round-neck-t-shirt/p/itme93rzrgdqaatk?pid=TSHE93RYD5FX5MPW",
          "http://www.flipkart.com/kakori-handcrafted-seated-musician-having-red-color-nickel-polish-finish-showpiece-17-cm/p/itmey9xffgzfv2yf?pid=SHIEY9XFGAWF3TU8",
          "http://www.flipkart.com/udaipur-art-gallery-wooden-decorative-platter/p/itmedxsytahbrvgw?pid=DEPEDXSYGHYWFHRT",
          "http://www.flipkart.com/pavvoin-lingerie-set/p/itmehdnyfahsfzd7?pid=LINEHDNYFGYZDBYN",
          "http://www.flipkart.com/fogg-fashion-store-3003-pk-modish-analog-watch-women/p/itmeay8wxry4ngm6?pid=WATEAY8W9HGKFUUQ",
          "http://www.flipkart.com/luba-hh41-stylo-analog-watch-women/p/itme96xzpbgxjwyw?pid=WATE96XZR5NRQFYX",
          "http://www.flipkart.com/pavechas-solid-striped-mangalagiri-cotton-sari/p/itme86dznwkkf2uv?pid=SARE86DZPAVZZ8S5",
          "http://www.flipkart.com/new-day-graphic-print-boy-s-round-neck-t-shirt/p/itme26pjf4haje2z?pid=TSHE26PJVENGBGFY",
          "http://www.flipkart.com/ben-carter-slim-fit-men-s-jeans/p/itmey8v924xzgubc?pid=JEAEY8V9YS3DB8HH",
          "http://www.flipkart.com/stanley-14-125-glass-cutter/p/itmdtxfgngugskxh?pid=CUTDTXFGNGUGSKXH",
          "http://www.flipkart.com/my-foot-women-heels/p/itmean427ctvyzze?pid=SNDEAN42XPSZS7MN",
          "http://www.flipkart.com/r18jewels-fashion-u-sparkle-delight-metal-bangle-set/p/itme4fg9tgnypnag?pid=BBAE4FG965UCG9PG",
          "http://www.flipkart.com/chevron-6-card-holder/p/itmdw4runxnje2bp?pid=CHDDW4RUMNAHUJCB",
          "http://www.flipkart.com/tales-stories-slim-fit-boy-s-jeans/p/itmeb3uyuhynk2dz?pid=JEAEB3UYMT2KNGE8",
          "http://www.flipkart.com/elligator-10-card-holder/p/itmdwg32har5ynnx?pid=CHDDWG32ZYENVXEX",
          "http://www.flipkart.com/best-6-card-holder/p/itmeyv2mzgzecgf4?pid=CHDEYV2MYNAV6KG6",
          "http://www.flipkart.com/rajasthan-crafts-abstract-single-quilts-comforters-multicolor/p/itme8yhumfabazdg?pid=BLAE8YHUYQG5JBBF",
          "http://www.flipkart.com/rajasthan-crafts-abstract-single-quilts-comforters-pink/p/itme8yhugzvdwrjs?pid=BLAE8YHU6APGPWDC",
          "http://www.flipkart.com/earth-ro-system-abstract-single-quilts-comforters-multicolor/p/itme7zk9gcr4ffay?pid=BLAE7ZK96GZGSYVG",
          "http://www.flipkart.com/geneva-gen-05-crystal-studded-analog-watch-women/p/itme7pyr5gh3c7bc?pid=WATE7PYRWT8ZEY5Y",
          "http://www.flipkart.com/pavechas-printed-kanjivaram-art-silk-sari/p/itme3wvs4af4e5dp?pid=SARE3WVSRJETB4NS",
          "http://www.flipkart.com/perucci-pc-3333purple-analog-watch-women/p/itme3fageqnpyhgt?pid=WATE3FAG5KAHZZJP",
          "http://www.flipkart.com/perucci-pc-3333yellow-analog-watch-women/p/itme3fagqtkvesva?pid=WATE3FAGBMUANYJZ",
          "http://www.flipkart.com/perucci-pc-310-analog-watch-men/p/itme3fag4w2cusxd?pid=WATE3FAGQZPGYYDN",
          "http://www.flipkart.com/chappin-nellson-cnl-50-white-rg-analog-watch-women/p/itmdw8e54evag3rw?pid=WATDW8E5PGWQUFWY",
          "http://www.flipkart.com/chappin-nellson-cnl-50-white-analog-watch-women/p/itmdw8e5zhgygfxy?pid=WATDW8E59X6EQTJH",
          "http://www.flipkart.com/port-fusion-football-shoes/p/itme84eaubh5hhau?pid=SHOE84EAMMT8WBW9",
          "http://www.flipkart.com/fs-mini-klub-solid-baby-boy-s-pathani-kurta/p/itme6nygg7tyq23m?pid=KTAE6NYGWKMXMX5G",
          "http://www.flipkart.com/xemex-st1025sl07-new-generation-analog-watch-women/p/itme6kygz4vvgyz7?pid=WATE6KYGHHMDFFMK",
          "http://www.flipkart.com/ireeya-abstract-single-coral-blanket-white-purple/p/itmey6cmrr9xd8yf?pid=BLAEY6CMPWHHNMZQ",
          "http://www.flipkart.com/my-newborn-solid-single-wrapper-assorted-muti-colors/p/itme5kysjaag4xyh?pid=BLAE5KYSAZ6QNEXV",
          "http://www.flipkart.com/total-care-tc-l830-screen-guard-nokia-lumia-830/p/itmeytxcfy8hhytb?pid=ACCEYTXCGP4W36VY",
          "http://www.flipkart.com/karpine-glass-screen-guard-nokia-lumia-830/p/itme26u2r4u2tefh?pid=ACCE26U2UDT3WUEN",
          "http://www.flipkart.com/karpine-clear-screen-guard-nokia-lumia-830/p/itmeyyx94u58fqgu?pid=ACCEYYX9Y5K8GGXZ",
          "http://www.flipkart.com/casotec-super-clear-screen-protector-guard-nokia-lumia-830/p/itmeyyfyyeyguhnv?pid=ACCEYYFYNFKKTZSZ",
          "http://www.flipkart.com/total-care-tcmtzc1fb-matte-front-back-protector-sony-xperia-z1-compact/p/itme2dczapr5g3bp?pid=ACCE2DCZ8TAFNEAP",
          "http://www.flipkart.com/nillkin-z3-84345-mirror-screen-guard-blackberry-z3/p/itmdyhphr3buzuvc?pid=ACCDYHPHP4EHDHYC",
          "http://www.flipkart.com/chicopee-women-flats/p/itmebgymxdn6heqg?pid=SNDEBGYMXGTC7BUG",
          "http://www.flipkart.com/love-baby-cartoon-set-towels/p/itmdn92fvcryprhg?pid=BTWDN9FZJWX4TBMZ",
          "http://www.flipkart.com/momento-regular-fit-men-s-jeans/p/itmdygm95y3yh6qq?pid=JEADYGM9AFTXAH7J",
          "http://www.flipkart.com/luba-bh23-stylo-analog-watch-men/p/itme9mxpyhzdhqp7?pid=WATE9MXPNCGYHEK3",
          "http://www.flipkart.com/mark-home-cotton-bath-towel/p/itmefz4vqhkgfd9m?pid=BTWEFZ4V9VFX8FAH",
          "http://www.flipkart.com/luba-ty47-stylo-analog-watch-men/p/itme9mxprmxt88zt?pid=WATE9MXPDDFGKUKK",
          "http://www.flipkart.com/swisstyle-ss-gr1409-blk-ch-flunky-analog-watch-men/p/itme8hu2zuwyghn7?pid=WATE8HU2ZJEJS92Z",
          "http://www.flipkart.com/goddess-women-women-s-animal-print-casual-shirt/p/itme34tjvzruawat?pid=SHTE34TJTDDGP8TH",
          "http://www.flipkart.com/trend18-women-s-animal-print-casual-shirt/p/itme6q3khzhfutzc?pid=SHTE6Q3KZ8TABHGN",
          "http://www.flipkart.com/younky-women-s-animal-print-casual-shirt/p/itmeypjaus2f55uk?pid=SHTEYPJASSGVYW3U",
          "http://www.flipkart.com/h2o-plus-eye-oasis-moisture-replenishment-treatment/p/itmd9ankuafpjxme?pid=ECMD9YGUDNHZCHZ5",
          "http://www.flipkart.com/president-school-waterproof-backpack/p/itmdxdn4qmbuwt9x?pid=BAGDXDN4ZHH7XTDE",
          "http://www.flipkart.com/indus-beats-striped-men-s-boxer/p/itmdzmhevsk4nesy?pid=BXRDZMHE4JPGHNN3",
          "http://www.flipkart.com/president-school-waterproof-backpack/p/itmdy6dxbghtpy8s?pid=BAGDY6DXVHYBVQPN",
          "http://www.flipkart.com/april6-woven-checkered-men-s-boxer/p/itmearabhs2rsgyv?pid=BXREARABPBQV65R5",
          "http://www.flipkart.com/president-school-waterproof-backpack/p/itmdy6dxy9gzh5de?pid=BAGDY6DXXV7FZHQY",
          "http://www.flipkart.com/april6-daniel-printed-men-s-boxer/p/itme798yx7wjhahz?pid=BXRE798Y96MZMP97",
          "http://www.flipkart.com/chaddy-buddy-gaand-faadu-printed-men-s-boxer/p/itme7yhj5jxesnqt?pid=BXRE7YHJVCUKHKF7",
          "http://www.flipkart.com/wineberry-show-off-checkered-men-s-boxer/p/itme6gazy39qpfyg?pid=BXRE6GAZFBFQJZBD",
          "http://www.flipkart.com/debenhams-jasper-conran-women-s-camisole/p/itmdsu5qxnvtmpcr?pid=CSPDSU5QKRPTGZGH",
          "http://www.flipkart.com/rana-watches-bw-prsmd-barbie-analog-watch-girls/p/itme5zjzuybbhpq4?pid=WATE5ZJZCGQUNQYF",
          "http://www.flipkart.com/primes-boys-girls-sandals/p/itmed4g9hmuryufz?pid=SNDED4G9SBG4BZY7",
          "http://www.flipkart.com/pick-pocket-women-casual-black-cotton-canvas-sling-bag/p/itmdz4z6hmu7m2eg?pid=SLBDZ4Z6PKKRGUKM",
          "http://www.flipkart.com/liza-women-wedges/p/itme5v33afm8kne4?pid=SNDE5V33PWZAGZDY",
          "http://www.flipkart.com/vogue-tree-women-casual-blue-canvas-sling-bag/p/itmeajztug95gevw?pid=SLBEAJZT8RVCKNMG",
          "http://www.flipkart.com/catwalk-women-wedges/p/itmdzk5fgpggwdbt?pid=SNDDZK5FHH85BUZN",
          "http://www.flipkart.com/pearl-paradise-kundan-necklace-brass-jewel-set/p/itme2j29z7v8tdpg?pid=JWSE2J29CCGMJFKH",
          "http://www.flipkart.com/pilot-roller-ball-pen/p/itmdtrg5zsfuwwhy?pid=PENDTRFZ3YW9SVVV",
          "http://www.flipkart.com/pilot-roller-ball-pen/p/itmdtrg5yrg9tsz3?pid=PENDTRFZGSCY6CBM",
          "http://www.flipkart.com/pearlz-ocean-pleasing-alloy-pearl-crystal-yellow-gold-bracelet/p/itme9jazj3dsw8v7?pid=BBAE9JAZJP8ZHNBX",
          "http://www.flipkart.com/swiss-charger-cable-de-synchro-micro-usb/p/itmeymfjq7zymzwv?pid=ACCEYMFJFNGPHMVW",
          "http://www.flipkart.com/remax-micro-usb-data-sync-charging-cable/p/itmefag9fnwh5hrk?pid=ACCEFAG9SWHGCHJD",
          "http://www.flipkart.com/avantree-micro-usb-retractable-cable/p/itmeygzvfmzazm9k?pid=ACCEYGZVZRV2HXNM",
          "http://www.flipkart.com/lg-ead63689301-usb-cable/p/itmebywy3zdtmcgh?pid=ACCEBYWYDYHDZYDK",
          "http://www.flipkart.com/uniball-sar-ball-pen/p/itmeafa9phymb7qu?pid=PENEAFA9SFMFMZGS",
          "http://www.flipkart.com/pearl-paradise-ink-drop-swarovski-crystal-silver-dangle-earring/p/itme4dsy7hhnnpfr?pid=ERGE4DSXWKPRMJPY",
          "http://www.flipkart.com/regent-analog-28-cm-dia-wall-clock/p/itme56uczsv9ssyf?pid=WCKE56UCWPSXZMZS",
          "http://www.flipkart.com/pearl-paradise-briolette-ruby-red-swarovski-crystal-stone-dangle-earring/p/itme3q7tfbma9pvf?pid=ERGE3Q7TWPZNVTRG",
          "http://www.flipkart.com/ecraftindia-analog-2-5-cm-dia-wall-clock/p/itme84h8jhwkthhh?pid=WCKE84H8CZW3H9TD",
          "http://www.flipkart.com/pearl-paradise-elements-swarovski-crystal-stone-dangle-earring/p/itme44u9apxgcjkb?pid=ERGE44U9QGSFRFGT",
          "http://www.flipkart.com/people-graphic-print-women-s-round-neck-t-shirt/p/itmea48zb9pvgj9c?pid=TSHEA48ZVHUBNESV",
          "http://www.flipkart.com/people-printed-women-s-round-neck-t-shirt/p/itmea48zxycabhdy?pid=TSHEA48Z73YRUPPH",
          "http://www.flipkart.com/pearl-paradise-briolette-moonlight-elements-swarovski-crystal-stone-dangle-earring/p/itme3rhdenndbrfn?pid=ERGE3RHDKXKNF9TS",
          "http://www.flipkart.com/pearl-paradise-complete-women-a-swarovski-crystal-silver-dangle-earring/p/itme865h57je7ehk?pid=ERGE865HYZYG3ZTX",
          "http://www.flipkart.com/pearl-paradise-long-black-diamond-swarovski-crystal-stone-dangle-earring/p/itme3q7tagzqrn7s?pid=ERGE3Q7TWYWJDHYU",
          "http://www.flipkart.com/regent-analog-28-cm-dia-wall-clock/p/itme56ucygpbeeqg?pid=WCKE56UC6FHRF8TH",
          "http://www.flipkart.com/regent-analog-31-cm-dia-wall-clock/p/itme23k4aszjtay7?pid=WCKE23K4EUMSGH4F",
          "http://www.flipkart.com/regent-analog-31-cm-dia-wall-clock/p/itme23k4fyyj87sm?pid=WCKE23K4FHXSXDFP",
          "http://www.flipkart.com/yepme-graphic-print-women-s-round-neck-t-shirt/p/itme6vh6qgfq73gh?pid=TSHE6VH6ZVHVGY7B",
          "http://www.flipkart.com/nevi-flower-swarovski-crystal-crystal-alloy-pendant/p/itmey2z4gh8yaerp?pid=PELEY2Z4F78JSKGE",
          "http://www.flipkart.com/nevi-swarovski-crystal-alloy-pendant/p/itmefh68j9heh3w5?pid=PELEFH68JH6FDERS",
          "http://www.flipkart.com/nevi-swarovski-crystal-crystal-alloy-pendant/p/itmeyfazgahhjhtc?pid=PELEYC9Z9FDZBDZU",
          "http://www.flipkart.com/suvarnadeep-rose-rhodium-zircon-sterling-silver-pendant/p/itme58u3hg96vgda?pid=PELE58U3FFP8EAAT",
          "http://www.flipkart.com/nevi-butterfly-swarovski-crystal-crystal-alloy-pendant/p/itme43z22b6exhcb?pid=PELE43Z2Z3XG55WB",
          "http://www.flipkart.com/xenio-gl86-tempered-glass-huawei-honor-6/p/itme59yx8kdcfjer?pid=ACCE59YXYNSCHX6J",
          "http://www.flipkart.com/neutron-hr-06-tempered-glass-huawei-honor-6/p/itme8jv7h4d24ggm?pid=ACCE8JV7WA69JWEW",
          "http://www.flipkart.com/molife-m-sltg-honor6plus-tempered-glass-huawei-honor-6-plus/p/itme66fe6khvauht?pid=ACCE66FE7EG4QH7P",
          "http://www.flipkart.com/aps-premium-scratch-protector-gl-hh6-tempered-glass-huawei-honor-6/p/itme7hkrzyvj68x4?pid=ACCE7HKR3QHGFYVF",
          "http://www.flipkart.com/yuuup-temp-2-30-tempered-glass-huawei-honor-6/p/itme7vef5zf6s6bk?pid=ACCE7VEFCM6ZZAYB",
          "http://www.flipkart.com/prixcracker-honor6-tempered-glass-huawei-honor-6/p/itme6fzpqrk4hqms?pid=ACCE6FZPCEEPAPGM",
          "http://www.flipkart.com/vmax-sc161-tempered-glass-huawei-honor-6/p/itme82yyhqhsxnkx?pid=ACCE82YYF7BJBXZ7",
          "http://www.flipkart.com/merastore-precious-priceless-rhodium-swarovski-crystal-alloy-pendant/p/itmdwnr5dxryt5td?pid=PELDWNR5EZNU6H4U",
          "http://www.flipkart.com/zwart-clinrov-32-l-medium-backpack/p/itme7b53gegxvbkg?pid=BKPE65ZGHGBZQBCY",
          "http://www.flipkart.com/president-shell-40-l-medium-backpack/p/itme63nzzpeqggyk?pid=BKPE63NZAEVFJ9VB",
          "http://www.flipkart.com/zwart-ryker-30-l-medium-backpack/p/itme7b5gdwtdgu7r?pid=BKPE6RDGZMNKCNFG",
          "http://www.flipkart.com/bleu-rucksack-60-l-large-backpack/p/itmeyn9a6ejvzbk9?pid=BKPEYN9AGHRCKEQY",
          "http://www.flipkart.com/president-shell-40-l-medium-backpack/p/itme63nzecyzzxhs?pid=BKPE63NZD2SKTWZP",
          "http://www.flipkart.com/wowmom-self-design-baby-boy-s-track-pants/p/itme3fyufphxkk3f?pid=TKPE2GSYFFVWFNPG",
          "http://www.flipkart.com/top-notch-solid-women-s-polo-neck-t-shirt/p/itmebjgpsthwmcfy?pid=TSHEBJGPDNYN6YRS",
          "http://www.flipkart.com/police-solid-men-s-polo-neck-t-shirt/p/itme9pup6pqzee7v?pid=TSHE9PUPSXWJDKMQ",
          "http://www.flipkart.com/pilot-ball-pen/p/itmddm4rj9m5dgfa?pid=PENDDM4QZXWDD8AX",
          "http://www.flipkart.com/regent-analog-31-cm-dia-wall-clock/p/itme23k4rd6jjz69?pid=WCKE23K4PDUHH5YH",
          "http://www.flipkart.com/indiano-women-s-leggings/p/itme9xbfhzh6begv?pid=LJGE9XBF7WXVQKGA",
          "http://www.flipkart.com/adidas-isolation-2-basketball-shoes/p/itmed7bmsxhtzafy?pid=SHODZJFFAM2H9CRC",
          "http://www.flipkart.com/planet-steel-plastic-dustbin/p/itmean9s6nhgrhfw?pid=DUBEAN9SCDCVGZBZ",
          "http://www.flipkart.com/heena-jewellery-alloy-brass-jewel-set/p/itmdxhxgq6ttdf8f?pid=JWSDXHXGZGR3ZWHG",
          "http://www.flipkart.com/pxl-men-s-solid-formal-shirt/p/itme5dfyzufhahjz?pid=SHTE5DFYHEGXBBSS",
          "http://www.flipkart.com/seven-days-men-s-solid-formal-linen-shirt/p/itmeyn8srkdf424f?pid=SHTEYN8S5FHNT99G",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmeahtwg89z7zth?pid=ACBEA449ZGSRGHXF",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmea449fcjhfg6d?pid=ACBEA449GB89ADNG",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmeahtwt9x2cnxz?pid=ACBEA449K34MHNGG",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmeahtwhatgdtrr?pid=ACBEA449ZTQWXSPV",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmeahtwxwtmhxzq?pid=ACBEA449EDYHB9ZA",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmea4499n3ymffm?pid=ACBEA449ZZJEYJFG",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmeahtvy9snetw9?pid=ACBEA449YYQTABFN",
          "http://www.flipkart.com/oye-top-girl-s-combo/p/itmebwtgzazxu2a5?pid=ACBEAGHHSUKWYKFX",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmea449pdbfkymh?pid=ACBEA449RSHGJ4GE",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7h9nrgwjr?pid=ACBEA449RNQG3NMX",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7pw6xfygy?pid=ACBEA4495H4WS89A",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7xhnghwmz?pid=ACBEA4494GNXG3TZ",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7mgh3whq5?pid=ACBEA4496TX8ZZV4",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7g8g6z8fq?pid=ACBEA4498A9CBFRX",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7nxnhjhmv?pid=ACBEA449WHCY6BRR",
          "http://www.flipkart.com/oye-top-skirts-girl-s-combo/p/itmecjt7whpggxqh?pid=ACBEA449AW9GBEUE",
          "http://www.flipkart.com/stylelite-women-s-printed-casual-shirt/p/itme9xbfuxdn79mm?pid=SHTE9XBFQDE4HPGF",
          "http://www.flipkart.com/catwalk-women-flats/p/itmdzk5fmzyftb9y?pid=SNDEYFWRUAVG9HGX",
          "http://www.flipkart.com/jeet-boy-s-kurta-pyjama-set/p/itme4bbpkgzxrkfv?pid=ETHEG78XAFUWG3CG",
          "http://www.flipkart.com/sea-shell-floral-pattern-cs102/p/itmecaeffrrfngz9?pid=CNSECAEFNH4KHQAN",
          "http://www.flipkart.com/kazamakraft-full-sleeve-solid-men-s-jacket/p/itmegypketch9ar7?pid=JCKEGYPKKWGZRBKN",
          "http://www.flipkart.com/timex-ti000i70600-analog-watch-men/p/itmdx7vguhtwxxqr?pid=WATDX7VGHZAP2GZG",
          "http://www.flipkart.com/titan-1641ym01-karishma-analog-watch-men/p/itmdtwvv6gufghf3?pid=WATDTWVV6GUFGHF3",
          "http://www.flipkart.com/playboy-bpb-1002-c-analog-watch-women/p/itmdm5ysqhkrykqu?pid=WATDM5YRFYJHCHBU",
          "http://www.flipkart.com/alberto-torresi-loafers/p/itmdw64mzhqzgfhy?pid=SHODF2C2SHHEFYRG",
          "http://www.flipkart.com/provogue-corporate-casuals/p/itmdmctu7dvwghtd?pid=SHODKYZ9C3HHKA3J",
          "http://www.flipkart.com/zoot24-loafers/p/itme94j25rhm2qw5?pid=SHOE94J3RHN7Z6AC",
          "http://www.flipkart.com/balujas-buntoe-loafers/p/itmdrwmxtxggwhy7?pid=SHODRWMX6YFTNG8V",
          "http://www.flipkart.com/quechua-arpenaz-100-hiking-shoes/p/itmdw67vstbv9fny?pid=SHODMFY6JGMSB3CR",
          "http://www.flipkart.com/harry-hill-broklyn-loafers/p/itme7bz8ftbtyyd9?pid=SHOE7BZ8KYCYNDCG",
          "http://www.flipkart.com/knotty-derby-diggory-boots/p/itmdxswwj8ran32f?pid=SHODXSWWQENJWHDK",
          "http://www.flipkart.com/zoot24-t22-dryolive-loafers/p/itme2qswhqudddxs?pid=SHOE2QSWZZFSCHAJ",
          "http://www.flipkart.com/metro-32-women-wedges/p/itmdty8hqvcfykgg?pid=SNDDTY8HHGHCR4ZG",
          "http://www.flipkart.com/zoot24-8186-3-casual-shoes/p/itme34yxnvjtevhh?pid=SHOE34YXWXZ9PCFF",
          "http://www.flipkart.com/true-soles-boots/p/itme558pjfzv7amp?pid=SHOE558ZECPBYKXG",
          "http://www.flipkart.com/allen-cooper-4507-party-wear/p/itmdx6xyyuzyattw?pid=SHODX6XYJXS2YXFY",
          "http://www.flipkart.com/lawman-pg3-persion-loafers/p/itme5dfvsyuzzvme?pid=SHOE5DFVH4RX6YAF",
          "http://www.flipkart.com/breakbounce-euler-canvas-shoes/p/itme7k6dq4kmnq6s?pid=SHOE6BEWJ3UEBDH9",
          "http://www.flipkart.com/hrx-29041-sneakers/p/itmdzyprfjjd2dye?pid=SHODZYPRHHQWFTF9",
          "http://www.flipkart.com/alberto-torresi-loafers/p/itmdw64m8ddtg7st?pid=SHODF2C2WGTMVQFZ",
          "http://www.flipkart.com/winkel-black-formal-lace-up-shoes/p/itme3hgtgjd8edkw?pid=SHOE3HGTYCWDACZ7",
          "http://www.flipkart.com/mactree-easy-life-lace-up-shoes/p/itme6krtvkatz3zj?pid=SHOE6KRTGQKP7FWM",
          "http://www.flipkart.com/armstrong-safety-defender-boots/p/itmeyy8afprvuhxk?pid=SHODXYYHVHYDQ5YN",
          "http://www.flipkart.com/zoot24-mamas-3-casual-shoes/p/itme24gjcpdsyqvx?pid=SHOE24GJYF8FAPWK",
          "http://www.flipkart.com/harry-hill-athens-loafers/p/itmee6uhew5kdzyx?pid=SHOEE6UHZZD83ZFN",
          "http://www.flipkart.com/jjc-ls-52-lens-hood/p/itmdg382pnmzffyb?pid=ACCDG38FUEYXRS5A",
          "http://www.flipkart.com/benera-omn-camouflage-boots/p/itme68h4pdt4nzjh?pid=SHOE68H5VYFUXUWK",
          "http://www.flipkart.com/sparx-sneakers/p/itmdxh79b985hv7n?pid=SHODZTGT6VB5YA8D",
          "http://www.flipkart.com/spunk-stylish-make-loafers/p/itme68nhqvdbpypu?pid=SHOE68NHF93EP4VH",
          "http://www.flipkart.com/omax-67mm-flower-lens-hood/p/itmdqrvchg7mhetw?pid=ACCDQRVC3FT9QWAU",
          "http://www.flipkart.com/provogue-corporate-casuals/p/itmdhzf8pbb4kaz9?pid=SHODHNUKYZZDYHRF",
          "http://www.flipkart.com/provogue-loafers/p/itmdzu53muehs35q?pid=SHODZU52VKGPEEGY",
          "http://www.flipkart.com/bosch-2-608-521-039-screwdriver-bit-set/p/itmdv9u9v8mvkfya?pid=SBSDUTY72YMGHEY6",
          "http://www.flipkart.com/benera-trekkesta-boots/p/itme632jvphhu3y7?pid=SHOE632JZBF4EF2H",
          "http://www.flipkart.com/jjc-lh-60-lens-hood/p/itmed842ppm9jdmc?pid=ACCED842W6KR595R",
          "http://www.flipkart.com/breakbounce-hulk-casual-shoes/p/itme6bewfbgmjn6j?pid=SHOE6BEWXGRHXZYC",
          "http://www.flipkart.com/true-soles-boots/p/itme558prxjg3fqz?pid=SHOE558ZNZWGFGPF",
          "http://www.flipkart.com/zoot24-tan-boots/p/itme2dg2npfszgk6?pid=SHOE2DG2VBCCY2Y5",
          "http://www.flipkart.com/basics-chukka-casual-shoes/p/itme3szwpykyxgkt?pid=SHOE3SZWY6USCQYN",
          "http://www.flipkart.com/provogue-corporate-casuals/p/itmdq3fucys3g6vq?pid=SHODQ3FUZVFEZFKQ",
          "http://www.flipkart.com/red-chief-rc2401-corporate-casuals/p/itmefwqgyh8nrq3f?pid=SHOEFWQGHEM2FEEG",
          "http://www.flipkart.com/knotty-derby-tan-diggory-boots/p/itmefh4tkf4ffgyr?pid=SHOEFH4VTVXDRGKG",
          "http://www.flipkart.com/provogue-loafers/p/itmdqp7zgzg6bpxq?pid=SHODQP7ZZRGUAXNX",
          "http://www.flipkart.com/yepme-slip-shoes/p/itme7u644dbgxzd4?pid=SHOE7U642BAVQGX6",
          "http://www.flipkart.com/bosch-2-607-001-513-extra-hard-screwdriver-bit-set/p/itmdv9uazecnmgaz?pid=SBSDUTY7JJXG2ZNK",
          "http://www.flipkart.com/yepme-slip-shoes/p/itme7u64xtrew4nj?pid=SHOE7U64ZNRXCBZF",
          "http://www.flipkart.com/jjc-lh-78e-lens-hood/p/itmddqfz8m2rygqe?pid=ACCDDQFZJGMXA58D",
          "http://www.flipkart.com/jjc-ls-55-lens-hood/p/itmdg382ghyanyx8?pid=ACCDG38FQQGWYHZD",
          "http://www.flipkart.com/bosch-2-607-001-531-extra-hard-screwdriver-bit-set/p/itmdv9u9srszvrae?pid=SBSDUTY7AZYZWSQS",
          "http://www.flipkart.com/bosch-2-608-521-041-screwdriver-bit-set/p/itmdv9u9c6pjzg8w?pid=SBSDUTY7NCF8T8TP",
          "http://www.flipkart.com/jjc-lh-74-lens-hood/p/itmddqfzhfedx9tb?pid=ACCDDQFZHKDB7YH5",
          "http://www.flipkart.com/jjc-lh-112-lens-hood/p/itmdnsfz92yyhv5v?pid=ACCDNSFXZHAFM2Z4",
          "http://www.flipkart.com/omax-58mm-flower-lens-hood/p/itmdqrvcztyvdhfs?pid=ACCDQRVCJQ3U5DUS",
          "http://www.flipkart.com/bosch-2-607-001-528-extra-hard-screwdriver-bit-set/p/itmdv9u9gc5mubgm?pid=SBSDUTY7VSABNSCK",
          "http://www.flipkart.com/petshop7-ps7db0025-l-pet-bed/p/itmeczehpcbrmyjq?pid=PEBECZEHCCAZERYV",
          "http://www.flipkart.com/bosch-2-607-001-514-extra-hard-screwdriver-bit-set/p/itmdv9u92duecvyt?pid=SBSDUTY7HTCTHD5V",
          "http://www.flipkart.com/jjc-lh-83f-lens-hood/p/itmdzbxhj7jtkzdg?pid=ACCDZBVY3W3EJ9YF",
          "http://www.flipkart.com/stybuzz-embroidered-decorative-cushion/p/itme8tqea6gthtsh?pid=PLWE8TQEW8KSMEQF",
          "http://www.flipkart.com/bosch-2-608-521-040-screwdriver-bit-set/p/itmdv9u9t49y4drg?pid=SBSDUTY7VBTVKMFF",
          "http://www.flipkart.com/bosch-2-608-521-043-screwdriver-bit-set/p/itmdv9u6eztafqbm?pid=SBSDUTY7XQRHXVRA",
          "http://www.flipkart.com/jjc-lh-73b-lens-hood/p/itmddqfz58fwedh7?pid=ACCDDQFZKMHHFSBG",
          "http://www.flipkart.com/jjc-lh-83j-lens-hood/p/itmddqfzfyrzpg4z?pid=ACCDDQFZNN6RJ7GS",
          "http://www.flipkart.com/funku-fashion-lace-up-shoes/p/itme8aphztuekjqg?pid=SHOE8APHN5RKHCDY",
          "http://www.flipkart.com/dgb-flexi-touch-x-11-usb-led-light/p/itmedx24bcd9ggm9?pid=USGEDX24UXPEEZEH",
          "http://www.flipkart.com/omax-ew-60c-canon-ef-s-18-55mm-f-3-5-5-6-lens-hood/p/itme7w6puhgkfy5s?pid=ACCE7W6P6NGHMGVG",
          "http://www.flipkart.com/spalding-cross-over-basketball-size-7/p/itmdmeyggyhczfqk?pid=BALDMEYGGYHCZFQK",
          "http://www.flipkart.com/bosch-2-608-521-038-screwdriver-bit-set/p/itmdv9u9bf7qeu5h?pid=SBSDUTY7FUJGFGZZ",
          "http://www.flipkart.com/canon-ew-83j-lens-hood/p/itmdgzethk5zwhrr?pid=ACCDGZDM9MQUUKER",
          "http://www.flipkart.com/ts4u-canvas-shoes/p/itme96z9xqkjdhzz?pid=SHOE96Z9KHM4WGAA",
          "http://www.flipkart.com/seastar-stadil-canvas-shoes/p/itme8kp4vj8mq9xx?pid=SHOE8KP4W9XCN3FJ",
          "http://www.flipkart.com/jjc-lh-83ii-lens-hood/p/itmdnsfzaaprncdy?pid=ACCDNSFXKWYDRK7Q",
          "http://www.flipkart.com/vinex-pacer-basketball-size-5/p/itmdgqb9gg7dc57h?pid=BALDGQB9GG7DC57H",
          "http://www.flipkart.com/bosch-2-607-001-526-extra-hard-screwdriver-bit-set/p/itmdv9u9cqcx9vd8?pid=SBSDUTY7DB4PDJJS",
          "http://www.flipkart.com/zdelhi-com-car-washer-z1-ultra-high-pressure/p/itme84edzw8a2ehe?pid=CWRE84EDSKFE8KF5",
          "http://www.flipkart.com/adidas-3-stripe-d-29-5-basketball-size-7/p/itmdhx8k5affmcgy?pid=BALDHX8K5AFFMCGY",
          "http://www.flipkart.com/shop-rajasthan-casual-solid-women-s-kurti/p/itme3sbuqprswbdh?pid=KRTE3SBUBNNRSK7G",
          "http://www.flipkart.com/nivia-destroyer-basketball-size-7/p/itmdxvabcqzsqehe?pid=BALDXVA6HJASHTDW",
          "http://www.flipkart.com/spalding-cross-over-basketball-size-5/p/itmdmeygwwrz4dac?pid=BALDMEYGWWRZ4DAC",
          "http://www.flipkart.com/little-kangaroos-girl-s-trousers/p/itmdyzqdza8hzjy4?pid=TRODYXVC8MXEWWQR",
          "http://www.flipkart.com/spalding-chicago-bulls-basketball-size-7-diameter-74-cm/p/itmdd3cz38d4xfkh?pid=BALDD3CZ38D4XFKH",
          "http://www.flipkart.com/rock-rocket-desktop-charger-6950290687051-usb-hub/p/itmecxhfqwuhacsj?pid=USGECXHFRRHFGRG2",
          "http://www.flipkart.com/mydress-mystyle-bulb-led-usb-light/p/itmedtm5r2hvqqdh?pid=USGEBZZ3Y567FZKP",
          "http://www.flipkart.com/shadowfax-table-air-fan-cooler-usb/p/itmee5zt7ngg6hjs?pid=USGEE5ZTTUZDK6Z8",
          "http://www.flipkart.com/finger-s-usb-fan-cum-power-bank-black-new/p/itmee4p5adhptxqs?pid=USGEE4P5BUGKHE2M",
          "http://www.flipkart.com/leather-king-adams-black-lace-up/p/itmey7hy6hgd33md?pid=SHOEY7HYDHGCWUPF",
          "http://www.flipkart.com/leather-king-oscar-black-lace-up/p/itmey7hynyggne7k?pid=SHOEY7HYNUXSNAT7",
          "http://www.flipkart.com/leather-king-blake-black-lace-up/p/itmey7hyjqjuqpwc?pid=SHOEY7HYCTPKZXUB",
          "http://www.flipkart.com/leather-king-alan-black-lace-up/p/itmey7hyyvzyh5jg?pid=SHOEY7HYSEZJQMMY",
          "http://www.flipkart.com/dgb-flexi-touch-x-11-usb-led-light/p/itmedx24bcd9ggm9?pid=USGEDX249AJ5XFKT",
          "http://www.flipkart.com/generix-hdmi-female-coupler-jointer-adapter-extender-gender-changer-gx-hdmi-coupler-usb-connector/p/itmecn4w45rdzdzy?pid=USGECN4WHY7M9MZJ",
          "http://www.flipkart.com/mydress-mystyle-bulb-led-usb-light/p/itmedtm5r2hvqqdh?pid=USGEBHHGHGUYVCZ8",
          "http://www.flipkart.com/lg-dh313os-5-1-home-theatre-system/p/itmedjcgx7jjuw5y?pid=HTHEDJCGQZ2RHXVZ",
          "http://www.flipkart.com/smiledrive-portable-key-chain-charger-iphone-5-5s-5c-usb-sync-charge-cable/p/itmdv9zeh8kku8zt?pid=USGDV9ZE7CM6PRRU",
          "http://www.flipkart.com/anker-uspeed-ah401-3-0-4-port-superspeed-68anhub-lb4a-usb-hub/p/itmdwbqzjusvqknt?pid=USGDWBQZ7FYD24WM",
          "http://www.flipkart.com/dgb-flexi-touch-x-11-usb-led-light/p/itmedx24bcd9ggm9?pid=USGEDX24YE8JV76H",
          "http://www.flipkart.com/dreamshop-flex-flexible-portable-usb-led-light/p/itmee3yxsb6zhtvt?pid=USGEE3YXGXN9FHUQ",
          "http://www.flipkart.com/dgb-flexi-touch-x-11-usb-led-light/p/itmedx24bcd9ggm9?pid=USGEDX24BCNC63FE",
          "http://www.flipkart.com/bruno-manetti-7007-lace-up-shoes/p/itme5hyu4mb7b5ng?pid=SHOE5HYUCXZXTSFE",
          "http://www.flipkart.com/spalding-nba-team-toranto-raptors-basketball-size-7/p/itmdt69zhwgwgw4v?pid=BALDK98MYRRTHZHJ",
          "http://www.flipkart.com/akshaj-lightweight-flexible-portable-adjustable-50000-hours-life-keyboard-laptop-pc-notebook-power-bank-book-reading-work-bed-usb-led-light/p/itmee7acakqagyme?pid=USGEE7ACNU4ZGY5E",
          "http://www.flipkart.com/shadowfax-table-air-fan-cooler-usb/p/itmee5zt7ngg6hjs?pid=USGEE5ZTJASSVBHV",
          "http://www.flipkart.com/mydress-mystyle-bulb-led-usb-light/p/itmedtm5r2hvqqdh?pid=USGEBZZ3SVFAFF5E",
          "http://www.flipkart.com/agrima-hub-port-a66-usb/p/itmeamadrzzzvhk8?pid=USGEAMADA8XHH2UM",
          "http://www.flipkart.com/spalding-tf-150-basketball-size-7/p/itmdt69e7trjzbhx?pid=BALDD3H7BUZDSQ77",
          "http://www.flipkart.com/kensington-33399eu-usb-hub/p/itmdu93bcdcfuqec?pid=USGDU93BCDCFUQEC",
          "http://www.flipkart.com/shoebook-genuine-leather-lace-up-shoes/p/itme3mzznfguu2sk?pid=SHOE3MZZYSGSFNHJ",
          "http://www.flipkart.com/grafion-women-wedges/p/itme8jz9dmxzzd4j?pid=SNDE8JZA27HBHUJR",
          "http://www.flipkart.com/foot-jewel-heel-brown-party-slip-women-wedges/p/itme33wx5mxnr2ey?pid=SNDE33WXXFHJUZPD",
          "http://www.flipkart.com/wave-walk-deuro-slip-shoes/p/itmeyayfzht6cagj?pid=SHOEYAYFVXGSD6ES",
          "http://www.flipkart.com/ishoes-kello-loafers/p/itmeyayfjyknycsu?pid=SHOEYAYFZYJEK2TN",
          "http://www.flipkart.com/eego-italy-sneakers/p/itmecd8fuxgenjkb?pid=SHOECD8GFBPPBPVM",
          "http://www.flipkart.com/shibha-footwear-women-wedges/p/itme9g8e3ygqunpk?pid=SNDE9G8EHTUXGSWF",
          "http://www.flipkart.com/teemoods-casual-woven-women-s-kurti/p/itme5ss9z4nzvpxa?pid=KRTE5SS9GKZ6FWDG",
          "http://www.flipkart.com/nandy-casual-striped-women-s-kurti/p/itme5f84agpgxcm9?pid=KRTE5F842WBVE5NQ",
          "http://www.flipkart.com/ishoes-real-brown-slip-shoes/p/itmdyyx9hjxpjrvw?pid=SHODYYX9N2ZM7CYY",
          "http://www.flipkart.com/wave-walk-royal-boots/p/itmeyb2f8j4z87cn?pid=SHOEYB2F9VK3GAZG",
          "http://www.flipkart.com/rodid-full-sleeve-solid-men-s-sweatshirt/p/itmebxyy9yyhag4y?pid=SWSEBXYY8KDH842P",
          "http://www.flipkart.com/strak-full-sleeve-striped-men-s-sweatshirt/p/itme2qqfkvugfghy?pid=SWSE2QQFZFAHU6HS",
          "http://www.flipkart.com/fila-full-sleeve-solid-men-s-reversible-sweatshirt/p/itmec8pjhbr3s6yx?pid=SWSEC8PKPENKTGVF",
          "http://www.flipkart.com/sports-52-wear-full-sleeve-solid-men-s-sweatshirt/p/itmeyfy7gff4ngvp?pid=SWSEYFY2E6P8HYSP",
          "http://www.flipkart.com/rodid-full-sleeve-solid-men-s-sweatshirt/p/itme22fpftgku4hg?pid=SWSE22FP6CPFS45P",
          "http://www.flipkart.com/sports-52-wear-full-sleeve-solid-men-s-sweatshirt/p/itmeyz72uhyg2gcd?pid=SWSEYZ7FNGYKDC7Y",
          "http://www.flipkart.com/cayman-full-sleeve-solid-men-s-sweatshirt/p/itme35bz6nyk42zy?pid=SWSE35BZH5UUWENW",
          "http://www.flipkart.com/wake-up-competition-full-sleeve-solid-men-s-sweatshirt/p/itme3n3y3as6wu7n?pid=SWSE3N3YRXWAYXKQ",
          "http://www.flipkart.com/redwave-360-degree-powered-rotation-bluetooth-selfie-stick/p/itmegdy6qcygkmud?pid=SSKEGDY6TVVGYPMQ",
          "http://www.flipkart.com/sivanna-baking-powder-rouge-highlighter/p/itmebhayu8rpwhkn?pid=HGLEA2G4YBK3JHZM",
          "http://www.flipkart.com/leaf-men-s-solid-formal-shirt/p/itmeaekyhhhfv8my?pid=SHTEAEKYBHPQTNZK",
          "http://www.flipkart.com/kalrav-men-s-solid-formal-shirt/p/itme8ybkfpkdk5vp?pid=SHTE7ZPZZY64JF72",
          "http://www.flipkart.com/jorzzer-roniya-men-s-solid-formal-party-wedding-casual-festive-shirt/p/itmecfak4zfahsmf?pid=SHTECFAKNASP6VVJ",
          "http://www.flipkart.com/karlsburg-men-s-checkered-formal-shirt/p/itmef3vt3zcfajb5?pid=SHTEF3VTKZT2FUSG",
          "http://www.flipkart.com/kingswood-men-s-self-design-formal-shirt/p/itmecyfavtuzak9b?pid=SHTECYFAZRXUGX96",
          "http://www.flipkart.com/invictus-men-s-striped-formal-shirt/p/itme2fbnxgmthffe?pid=SHTE2FBNHEJQSZUF",
          "http://www.flipkart.com/kuons-avenue-men-s-solid-formal-shirt/p/itmdzdrpkwxye3b3?pid=SHTDZDRP2JGKKUWT",
          "http://www.flipkart.com/kayara-collection-men-s-striped-formal-shirt/p/itmecwfbfzd3cnrc?pid=SHTECWFBJWJ4WXRG",
          "http://www.flipkart.com/kraasa-men-s-solid-formal-shirt/p/itme6rht26ncyyye?pid=SHTE6RHTHFGZE6VV",
          "http://www.flipkart.com/ishin-men-s-solid-formal-shirt/p/itme6p4d2zhgbvdr?pid=SHTE6P4DSFYZGGGU",
          "http://www.flipkart.com/indian-weller-men-s-striped-formal-shirt/p/itme5c2hp9hkvkzm?pid=SHTE5C2HZYNMJ8SX",
          "http://www.flipkart.com/leaf-men-s-solid-formal-shirt/p/itme9uzcrtguqjbx?pid=SHTE9UZBRZNTUQTN",
          "http://www.flipkart.com/kraasa-men-s-solid-formal-shirt/p/itme6rht26ncyyye?pid=SHTE6RHTYXHMZ5FR",
          "http://www.flipkart.com/shaun-trackpant-solid-girl-s-track-pants/p/itme9grbpwzvzgfr?pid=TKPE9GRBBH8G4SHX",
          "http://www.flipkart.com/beadworks-acrylic-alloy-bracelet/p/itme4ds7uthmzzfn?pid=BBAE4DS7AJPPPZ96",
          "http://www.flipkart.com/trilokani-sport-walking-shoes/p/itme8cwnhsgajmvs?pid=SHOE58EKXSEYAYX6",
          "http://www.flipkart.com/sheetalworld-microfiber-set-towels/p/itme3vwmpfahugcn?pid=BTWE3VWM9HENTJXC",
          "http://www.flipkart.com/trident-cotton-set-towels/p/itmeyhehuztmczgu?pid=BTWEYHEHZGE7JTDJ",
          "http://www.flipkart.com/select-sporty-walking-shoes/p/itmdz9akc4gc53fk?pid=SHODZ9AKGHEYPWGT",
          "http://www.flipkart.com/select-sporty-running-shoes/p/itmdzdfbd5h9cagx?pid=SHODZDFBUZVTNZUH",
          "http://www.flipkart.com/mafatlal-cotton-bath-towel/p/itmdzhjgzhkphdsg?pid=BTWDZHJGZHKPHDSG",
          "http://www.flipkart.com/mafatlal-cotton-bath-towel/p/itmdzhjgsfj4sq8g?pid=BTWDZHJGSFJ4SQ8G",
          "http://www.flipkart.com/riana-copper-bangle/p/itmeaxfqkdnw9ghy?pid=BBAEAXFQHHMF3EYZ",
          "http://www.flipkart.com/bigshoponline-cotton-bath-towel/p/itmebx2snxgfnyhq?pid=BTWEBX2SHBRWEZYW",
          "http://www.flipkart.com/intex-happy-animal-chair-assortment-inflatable-air/p/itmdfzmhegt7hudg?pid=IFPDFZMGQZCHXVR5",
          "http://www.flipkart.com/trident-cotton-set-towels/p/itmeyheh8wvqcduv?pid=BTWEYHEHGEHZP4RV",
          "http://www.flipkart.com/trident-cotton-set-towels/p/itme7gtgrhefckvj?pid=BTWE7GTGSHBTEZC8",
          "http://www.flipkart.com/goldnera-alloy-rose-gold-bangle-set/p/itme5akcrkabfhkg?pid=BBAE5AKCDFDZ2FWQ",
          "http://www.flipkart.com/sassoon-cotton-bath-towel/p/itme2qpequ6s3egg?pid=BTWE2QPEY9F8ZBGX",
          "http://www.flipkart.com/mandhania-cotton-bath-towel/p/itme5qugdy6psdsh?pid=BTWE5QUGZHGG8YZH",
          "http://www.flipkart.com/sassoon-cotton-bath-towel/p/itmdymy2q2hqxqna?pid=BTWDYMY2QQGMGSHY",
          "http://www.flipkart.com/mast-harbour-striped-round-neck-casual-men-s-sweater/p/itmeb9buhztphksy?pid=SWTEB9BUZ7GPWZ4G",
          "http://www.flipkart.com/crunchy-fashion-alloy-bangle-set/p/itmdr67feycquxe7?pid=BBADR66XXFKCHXCM",
          "http://www.flipkart.com/british-cross-striped-round-neck-casual-men-s-sweater/p/itmeafygvkcw9pum?pid=SWTEAFYHGPFNGHUS",
          "http://www.flipkart.com/british-cross-striped-round-neck-casual-men-s-sweater/p/itmeafyhs9grvg6v?pid=SWTEAFYHHBKXUBF3",
          "http://www.flipkart.com/alysa-alloy-pearl-yellow-gold-rhodium-bracelet-set/p/itmeagtc526nkggh?pid=BBAEAGTC3ABCHVEY",
          "http://www.flipkart.com/trident-cotton-face-towel/p/itme6n5shvgbsuug?pid=BTWE6N5SXYEJHZPB",
          "http://www.flipkart.com/intex-kids-inflatable-air-chair/p/itmdfzmh2qcz5hza?pid=IFPDFZMGZBEZ3KCZ",
          "http://www.flipkart.com/lukluck-cotton-bath-towel/p/itmecdbwjbwezczj?pid=BTWECDBWTUETCFCK",
          "http://www.flipkart.com/amber-cotton-hand-towel/p/itme3smgmmefbv6t?pid=BTWE3SMGGTGTSMNF",
          "http://www.flipkart.com/sweet-angel-printed-girl-s-track-pants/p/itmeypeczkh5cgmj?pid=TKPEYPECGWCK5HH7",
          "http://www.flipkart.com/crazytowear-metal-bangle-set/p/itmeanyzcgvf4aen?pid=BBAEANYZ3FGWQY2Z",
          "http://www.flipkart.com/alysa-brass-copper-cubic-zirconia-emerald-18k-yellow-gold-rhodium-bangle-set/p/itmeby58ahcyazhn?pid=BBAEBY58VYWPEMWG",
          "http://www.flipkart.com/zobello-leather-bracelet/p/itmeag4dqyyhzvau?pid=BBAEAG4DN8TYH7EH",
          "http://www.flipkart.com/jewels-mountain-sterling-silver-zircon-bracelet/p/itme8qefhzypmatf?pid=BBAE8QEFYAQFSPHP",
          "http://www.flipkart.com/duke-striped-casual-men-s-sweater/p/itmeyz7y3zfzswsx?pid=SWTEYZ7YWYG77NPD",
          "http://www.flipkart.com/duke-striped-casual-men-s-sweater/p/itmdzchnz8fhh9mn?pid=SWTDZCHNEZAGKVHZ",
          "http://www.flipkart.com/duke-striped-casual-men-s-sweater/p/itmeyz7yhgz8wyck?pid=SWTEYZ7YNGBQATFY",
          "http://www.flipkart.com/mb-cotton-set-towels/p/itmeyfa92urgfe8z?pid=BTWEYFA942QUCJ6Q",
          "http://www.flipkart.com/jbg-home-store-cotton-face-towel/p/itme8fgzz7de87py?pid=BTWE8FGZNHZTFPMT",
          "http://www.flipkart.com/mandhania-cotton-bath-towel/p/itme5qugtrkphyfm?pid=BTWE5QUG296M8Q39",
          "http://www.flipkart.com/soulxpressions-metal-pearl-bracelet/p/itmea8fdvvpbgzpz?pid=BBAEA8FD33BZXTEZ",
          "http://www.flipkart.com/zobello-leather-bracelet/p/itmeag4dshqqheau?pid=BBAEAG4DMUBBYUKA",
          "http://www.flipkart.com/trident-cotton-set-towels/p/itmeyc5vpk7kh74g?pid=BTWEYC5VMGHUZBDV",
          "http://www.flipkart.com/peora-sanmita-gold-plated-alloy-jewel-set/p/itmdytmzdfcudhfc?pid=JWSDYTMZKQ5TBSQY",
          "http://www.flipkart.com/eprilla-solid-v-neck-casual-men-s-sweater/p/itmedau6kjxzahtz?pid=SWTEDAU6RPWWYMJP",
          "http://www.flipkart.com/montana-mtn-94-spray-paint-bottle/p/itmdzuermtjyc97r?pid=PTSDZUERRKENB2FV",
          "http://www.flipkart.com/bombay-dyeing-cotton-bath-towel/p/itmdyh2t53zqrzyw?pid=BTWDYH2TV374GBWR",
          "http://www.flipkart.com/trident-cotton-bath-towel/p/itme6hd2vqcfnzs7?pid=BTWE6HD25KATEMZQ",
          "http://www.flipkart.com/trident-cotton-bath-towel/p/itme6hd2rz7xemcx?pid=BTWE6HD2UQA5HBHY",
          "http://www.flipkart.com/raees-wayfarer-sunglasses/p/itmejupqytseecz5?pid=SGLEJUPQYCPT7QGU",
          "http://www.flipkart.com/pu-easy-life-monk-strap/p/itmebyxxdzpvhehf?pid=SHOEBYXXZQYHGJJY",
          "http://www.flipkart.com/lgrl-women-s-leggings/p/itmegjj23rvk6zpv?pid=LJGEGJJ3A3YPGNMP",
          "http://www.flipkart.com/tara-lifestyle-slim-fit-boy-s-jeans/p/itmegwznfdfwrgnj?pid=JEAEGWZZZZHV77CU",
          "http://www.flipkart.com/nivia-school-lace-up-shoes/p/itme9sepgegyrghg?pid=SHOE9SEPYF85JXNQ",
          "http://www.flipkart.com/asian-walking-shoes/p/itmegwvesacgjv58?pid=SHOEGWVEARZFYHUZ",
          "http://www.flipkart.com/asian-lace-up-shoes/p/itmeagv3cqrthyuk?pid=SHOEAJHWWBJBB8DH",
          "http://www.flipkart.com/vijayanti-international-shin-guard/p/itmdehtqzf7xztez?pid=GUADCG9TAWKF49RZ",
          "http://www.flipkart.com/pu-right-tennis-black-school-shoes/p/itmecyrfyfhn5ufn?pid=SHOECYRFRZW9KDY2",
          "http://www.flipkart.com/bellegirl-floral-print-baby-girl-s-boxer/p/itmefp5mkzdpgsy6?pid=BXREFP5MUQBJU2DE",
          "http://www.flipkart.com/rex-monk-strap/p/itmeewnzvzyk49fp?pid=SHOE8YNTDQGYYSHR",
          "http://www.flipkart.com/rex-school-shoes/p/itmeewz7hddzwhjz?pid=SHOE83BTZFSTW9FD",
          "http://www.flipkart.com/zebie-spb100096-solar-12000-mah-power-bank/p/itmehd23x67yjzda?pid=PWBEHD23J2HXNMBT",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme87gjcdd9qqxx?pid=BRAEGZYDHFHZ6WRN",
          "http://www.flipkart.com/clovia-women-s-full-coverage-bra/p/itme8z3yhtcchcvq?pid=BRAEGZY9JWRP7SZT",
          "http://www.flipkart.com/mobiware-mw5b-ultra-slim-5000mah-powerbank-5000-mah/p/itmeh23p5anqxedq?pid=PWBEH239K4WVXXMM",
          "http://www.flipkart.com/skovin-boy-school-shoes-lace-up/p/itmegdt7vrmzgqxr?pid=SHOEGDT7PZMGHKQF",
          "http://www.flipkart.com/mobiware-mw4p-4000-mah-pocket-powerbank/p/itmeh24yaf2het8b?pid=PWBEH24XHG2YBYED",
          "http://www.flipkart.com/spycom-wireless-3-5mm-bluetooth-audio-music-receiver-mic-handsfree-stereo-output-car-kit/p/itmef8czwfvg67p6?pid=ACCEF8CZKFEXZKFM",
          "http://www.flipkart.com/smiledrive-snuggle-arm-shaped-stuffed-pillow-toy-25-inch/p/itmdtgqzbzphfh8k?pid=STFDTGQZGEVP2HAM",
          "http://www.flipkart.com/incolor-metalic-lipstick-19-3-8-g/p/itme26u5rtq63fjq?pid=LSKE26U5F87S8GWH",
          "http://www.flipkart.com/yna-checkered-double-quilts-comforters-red/p/itmdz9cw337rqatd?pid=BLADZ9CWEWMBEQZN",
          "http://www.flipkart.com/united-bags-pencil-pi-backpack-35-l/p/itme687fdt7pvzfp?pid=BKPE687F7GK6AYU2",
          "http://www.flipkart.com/sophies-shisha-assorted-hookah-flavor/p/itme4p3ywv8gbk2t?pid=HOFE4P3YD2BFJYYT",
          "http://www.flipkart.com/taaza-garam-6-axis-seeker-2-4ghz-remote-control-drone/p/itmee9ggby8mv26k?pid=RCTEE9GGHDFFWEF9",
          "http://www.flipkart.com/agaro-beard-mt-6014-trimmer-men/p/itmdnazt78derrem?pid=SHVDNAZR4CJHKTQK",
          "http://www.flipkart.com/elfani-brilliance-lip-color-3-5-g/p/itmeebkzbuzad5xf?pid=LSKEDKXZBSVQ883C",
          "http://www.flipkart.com/united-bags-cross-chain-35-l-medium-laptop-backpack/p/itmeyqhbxagz8wxf?pid=BKPEYQHBGRH6KYMH",
          "http://www.flipkart.com/brite-rechargeable-490-trimmer-men/p/itmeygzushmrgqwm?pid=SHVEYGZUH6MAGSPS",
          "http://www.flipkart.com/asist-health-care-plain-single-electric-blanket-blue/p/itmed8fwth7fy829?pid=BLAED8FWSFTEZARZ",
          "http://www.flipkart.com/syska-led-lights-5-w-bulb/p/itme7fgjpdhrey7z?pid=BLBE7FGJKZHQYNJF",
          "http://www.flipkart.com/clarks-women-flats/p/itmdvpanxghutfez?pid=SNDDVP9CYXHTZ7XC",
          "http://www.flipkart.com/unnati-floral-double-top-sheet-multicolor/p/itmefnycuazgmzgz?pid=BLAEFNYCRGTHXXEX",
          "http://www.flipkart.com/brunte-special-design-reddragon-big-rc-helicopter-light-remote-charger/p/itme5bz4eqchqzgt?pid=RCTE5BZ4HTGYDQZC",
          "http://www.flipkart.com/leaf-tork-2-5-l-medium-backpack/p/itme4gf4cqephasf?pid=BKPE4GF4HMYZRQAM",
          "http://www.flipkart.com/kemei-washable-body-groomer-km-6166-trimmer-men/p/itme5kz9zhzygmv3?pid=SHVE5KZ9AYH4YSJ5",
          "http://www.flipkart.com/dell-sports-laptop-backpack/p/itme25gdjhdr8bzf?pid=BKPE25GC2ZFVGGNU",
          "http://www.flipkart.com/incolor-metalic-lipstick-n15-3-8-g/p/itme36a6xzymdn6b?pid=LSKE36A69ZNY64DG",
          "http://www.flipkart.com/safari-zoom-25-l-small-backpack/p/itmeb2pfggeghggk?pid=BKPEB2PFJPENHHJK",
          "http://www.flipkart.com/mz-nova-most-advanced-2in1-rechargeable-nhc-401-trimmer-men/p/itme9vhfb8d5k5kq?pid=SHVE9VHFFYAY8HBT",
          "http://www.flipkart.com/wipro-5-w-led-6500k-cool-day-light-bulb/p/itmdyga9nvf5tbec?pid=BLBDYGA8SAAWHNVH",
          "http://www.flipkart.com/puma-primary-3-l-backpack/p/itme9r5dw2zfdkzj?pid=BKPE9R5CWH6CNCWM",
          "http://www.flipkart.com/sophies-shisha-assorted-hookah-flavor/p/itme4p3yfz4c2jdz?pid=HOFE4P3YVFHFFMGS",
          "http://www.flipkart.com/dr-scholl-rachel-women-flats/p/itmeegv6utqq79sn?pid=SNDDVN24AHEAYBYM",
          "http://www.flipkart.com/gifts-arts-remote-control-jeep/p/itme3bsayhzxaztq?pid=RCTE3BSA9AQGCZXX",
          "http://www.flipkart.com/unnati-floral-double-top-sheet-multicolor/p/itmefnycgcjpzep7?pid=BLAEFNYCWVERCSRX",
          "http://www.flipkart.com/cult-fiction-polka-print-women-s-round-neck-t-shirt/p/itme3hjwfvtzdyzu?pid=TSHE3HJWSZ2AZGPR",
          "http://www.flipkart.com/bombay-high-women-s-printed-formal-shirt/p/itmdua8d2aqbc87q?pid=SHTDUA8D3GGBMNTJ",
          "http://www.flipkart.com/alpha-lady-embroidered-women-s-gathered-skirt/p/itmeap5ugyzh8bmc?pid=SKIEAP5UYKWH9VZP",
          "http://www.flipkart.com/slb-020rp-10-l-backpack/p/itme536fgvx9s9qb?pid=BKPE536FHSNYE85F",
          "http://www.flipkart.com/united-bags-1000d-rainbow-35-l-medium-backpack/p/itmeegdndpfscbgj?pid=BKPEBAUXZVMGHBUG",
          "http://www.flipkart.com/x360-905-24-675-l-backpack/p/itmdxv8hjtjaphv2?pid=BKPDXV8HNGJJRBWC",
          "http://www.flipkart.com/unnati-abstract-single-top-sheet-multicolor/p/itmefhq3uqhcrwpc?pid=BLAEFHQ3DNE82GHZ",
          "http://www.flipkart.com/complete-italian-learn-teach-yourself-enhanced-ebook-new/p/itme56yfcvfyakf4?pid=DGBDFGE4UJQDEZSJ",
          "http://www.flipkart.com/syon-cotton-floral-double-bedsheet/p/itmegwt4xamyjsgz?pid=BDSEGWT4FQHRSENN",
          "http://www.flipkart.com/syon-cotton-floral-double-bedsheet/p/itmegwt4uwfxzdxj?pid=BDSEGWT4WMZANBMH",
          "http://www.flipkart.com/syon-cotton-floral-double-bedsheet/p/itmegwt5wnygxxb8?pid=BDSEGWT5Q2TNUKHX",
          "http://www.flipkart.com/syon-cotton-floral-double-bedsheet/p/itmegwt5gkzwy9pj?pid=BDSEGWT58RQP4DXV",
          "http://www.flipkart.com/aarti-collections-women-s-self-design-casual-formal-denim-light-blue-shirt/p/itmejp22jzguphd6?pid=SHTEJP22GH6GHTKR",
          "http://www.flipkart.com/maharaja-timer-electric-tandoor/p/itmeehe68jumdrea?pid=FDMEEHE6PWNXWYMK",
          "http://www.flipkart.com/deep-kitchen-press-steel-grater-slicer/p/itme8kfbzsvahsbw?pid=GRTE8KFBQ8RGDNT7",
          "http://www.flipkart.com/sayitloud-men-s-vest/p/itmeb2qmbmkfg9zd?pid=VESEGRBBR2ZGYCQW",
          "http://www.flipkart.com/sayitloud-men-s-vest/p/itme5k4krhndycy5?pid=VESEGRBARYJUSGJG",
          "http://www.flipkart.com/fume-men-women-wrist-band/p/itmdqfwdgfc2drje?pid=WTBDPEWSAHZZSHB3",
          "http://www.flipkart.com/royal-men-s-kurta-churidar-set/p/itmej6f5hs4vfwqm?pid=ETHEJ6F5BGTXT4RK",
          "http://www.flipkart.com/elephant-brand-3-fold-polka-dotted-prints-manual-open-umbrella/p/itmegff6f4zjpkap?pid=UMBEGFF6VMYKCFVZ",
          "http://www.flipkart.com/zovi-regular-fit-men-s-trousers/p/itmdzntf2bgcx2x8?pid=TRODZNTFF9EXWB5S",
          "http://www.flipkart.com/snehkriti-traditional-ethnic-potli/p/itmefpyt5vzqxyya?pid=PPSEFPYTHEZGXHUS",
          "http://www.flipkart.com/cenizas-western-mocassins/p/itme6wpygammrvkt?pid=SHODTSJPKFRPAZKH",
          "http://www.flipkart.com/nova-professional-hair-ns216-trimmer-clipper-shaver-men/p/itmefbh8zqsfswh2?pid=SHVEFNYPDZDWQCZW",
          "http://www.flipkart.com/balaji-velvet-sofa-cover/p/itmeexzy8fjwyz7p?pid=SLIEEXZYYFHXTCZA",
          "http://www.flipkart.com/mast-harbour-skinny-fit-women-s-jeans/p/itmec87zzcxvq2k4?pid=JEAEC87ZBHGBMVZC",
          "http://www.flipkart.com/blackberrys-solid-single-breasted-casual-men-s-blazer/p/itmehj6zm9xvxaby?pid=BZREHJ6Z8WJQHFPX",
          "http://www.flipkart.com/clovia-lingerie-set/p/itme8f4asqjyjupw?pid=LINEHAGVMJ7QUUFJ",
          "http://www.flipkart.com/convenience-vm46-headphone-xiomi-mi4-mi4i-signature-stereo-wired-headphones/p/itmegkdguumzrcvk?pid=ACCEGKDGVZWHYV5H",
          "http://www.flipkart.com/esteem-boy-s-drawer/p/itmedzcajrhk9sqa?pid=BLREDZCAQN5FRGTF",
          "http://www.flipkart.com/transcend-premium-memory-ddr2-2-gb-1x2gb-pc-sdram-jm800qlu-2g/p/itmd2rypzhmmcjwa?pid=RAMEGFGCHMH8AN8W",
          "http://www.flipkart.com/mua-makeup-academy-sweet-sheen-dusky-rose/p/itme8yqddhjhtry4?pid=LPBEFHWZMT3GMH4U",
          "http://www.flipkart.com/nova-kt-728s-electric-kettle/p/itmdg5cqhuhmgqj7?pid=EKTDG5C5QSADZZ8J",
          "http://www.flipkart.com/miss-chase-women-s-a-line-dress/p/itmdt9rcszuasbnw?pid=DREDT9RCUGEJ6BQU",
          "http://www.flipkart.com/liz-lange-women-s-a-line-dress/p/itme9zkfzw7femcz?pid=DREE9ZKYZJHBS45P",
          "http://www.flipkart.com/maggie-women-s-shift-dress/p/itmeccmnzryqmftn?pid=DREECCMNGJUWZDVF",
          "http://www.flipkart.com/miss-chase-women-s-sheath-dress/p/itmdv8hgrmqjp5yn?pid=DREDV8HG7Z8BFFXZ",
          "http://www.flipkart.com/maggie-women-s-empire-waist-dress/p/itmeccmnhy7hqnq7?pid=DREECCMNZSVNVHHK",
          "http://www.flipkart.com/isadora-women-s-shift-dress/p/itme7ue34hbccjt5?pid=DREE7UE3SH2GGG2F",
          "http://www.flipkart.com/lady-stark-women-s-a-line-dress/p/itme58qr9eencufb?pid=DREE58QRW5T5T8MK",
          "http://www.flipkart.com/miss-chase-women-s-bandage-dress/p/itmdv8hgfshe6fsz?pid=DREDV8HGDHM8D6PU",
          "http://www.flipkart.com/karishma-women-s-a-line-dress/p/itmdzztunfcwdtqr?pid=DREDZZTUSAHPHGUS",
          "http://www.flipkart.com/miss-chase-women-s-high-low-dress/p/itmdvc24mjmpmzt7?pid=DREDVC24VGNSAKFZ",
          "http://www.flipkart.com/maggie-women-s-gathered-dress/p/itmeccmn6thfruqw?pid=DREECCMNACW7K73W",
          "http://www.flipkart.com/miss-chase-women-s-bandage-dress/p/itme5tgrfepzz5mx?pid=DREE5TGRJWKBAURG",
          "http://www.flipkart.com/hugo-chavez-women-s-peplum-dress/p/itme8aqxjffpgtu2?pid=DREE8AQXPWYHDYGR",
          "http://www.flipkart.com/mayra-women-s-a-line-dress/p/itme88knmfgwajfb?pid=DREE88KNZCHEBWSM",
          "http://www.flipkart.com/latin-quarters-women-s-shift-dress/p/itmdudjk2ggazdey?pid=DREDUDJKYY8PFJJZ",
          "http://www.flipkart.com/mayra-women-s-a-line-dress/p/itme8juhyh8kxnq2?pid=DREE8JUHY9YPVBFG",
          "http://www.flipkart.com/hugo-chavez-women-s-maxi-dress/p/itme6d3evxhrs8zd?pid=DREE6D3EAYAHMAPE",
          "http://www.flipkart.com/hugo-chavez-women-s-maxi-dress/p/itme6d3e6rbfxj3g?pid=DREE6D3EXMS7DAZH",
          "http://www.flipkart.com/ladybug-women-s-a-line-dress/p/itmdzzvyu9d2jabs?pid=DREDZZVYZB4V9DGN",
          "http://www.flipkart.com/hugo-chavez-women-s-sheath-dress/p/itmeaxe3q9gbuf94?pid=DREEAXE3VAX3GY9Y",
          "http://www.flipkart.com/maggie-women-s-maxi-dress/p/itmeccmnhe9n2329?pid=DREECCMNWCGEMQYP",
          "http://www.flipkart.com/karishma-women-s-a-line-dress/p/itmdzhyujhhhrecg?pid=DREDZHYUNBFXRK3H",
          "http://www.flipkart.com/maggie-women-s-shift-dress/p/itme9ehegppaxgg3?pid=DREE9EHEWXZYSCDU",
          "http://www.flipkart.com/miss-chase-women-s-a-line-dress/p/itme3hgekeqr7gzs?pid=DREE3HGEK7VH4ZWP",
          "http://www.flipkart.com/hugo-chavez-women-s-bandage-dress/p/itmeaxe3d6rk2zsp?pid=DREEAXE3W4GCYENW",
          "http://www.flipkart.com/maggie-women-s-a-line-dress/p/itmeccmn5tdxdmbd?pid=DREECCMNMNBWJUMX",
          "http://www.flipkart.com/hugo-chavez-women-s-maxi-dress/p/itme6vtrj9txwxcx?pid=DREE6VTRBEX44KBP",
          "http://www.flipkart.com/lady-stark-women-s-maxi-dress/p/itmebsfyg6czef3p?pid=DREEBSFYMUHT9NJX",
          "http://www.flipkart.com/miss-chase-women-s-bandage-dress/p/itme4bhgdkjnsuhz?pid=DREE4BHHQKZSNPNG",
          "http://www.flipkart.com/legona-women-s-sheath-dress/p/itmecacvz4wgc3yv?pid=DREECACWVFWUG5P2",
          "http://www.flipkart.com/karyn-women-s-high-low-dress/p/itme9qy9qsexzf2p?pid=DREE9QY9NFZ2J7RD",
          "http://www.flipkart.com/karishma-women-s-gathered-dress/p/itmdxxnfvtekf8w4?pid=DREDXXNFYCD2VEXN",
          "http://www.flipkart.com/hugo-chavez-women-s-maxi-dress/p/itme8ahxvfzqkdzh?pid=DREE8AHXBEQN43BA",
          "http://www.flipkart.com/miss-chase-women-s-a-line-dress/p/itme2zmue8wpgdfu?pid=DREE2ZMUBG4D4JZS",
          "http://www.flipkart.com/indi-bargain-women-s-a-line-dress/p/itme5m4zbhgssr9v?pid=DREE5M4Z4YKVRTGR",
          "http://www.flipkart.com/meira-women-s-a-line-dress/p/itme6yzzh2dbqq5y?pid=DREE6YZZQEQDK525",
          "http://www.flipkart.com/ladybug-women-s-a-line-dress/p/itmdsuzxwy4vj38r?pid=DREDSUZWUZMYFJMF",
          "http://www.flipkart.com/honey-pantaloons-women-s-a-line-dress/p/itme8mxvhb6npqs4?pid=DREE87ESGZM4KEJF",
          "http://www.flipkart.com/mayra-women-s-a-line-dress/p/itme88kmsm64uhwy?pid=DREE88KMCGFCEHJR",
          "http://www.flipkart.com/miss-chase-women-s-sheath-dress/p/itmdvgbgmcqadmy5?pid=DREDVGBGWKSAAVVG",
          "http://www.flipkart.com/hugo-chavez-women-s-bandage-dress/p/itmeyjz7mswqxyxh?pid=DREE7UCDU7JASMGR",
          "http://www.flipkart.com/indi-bargain-women-s-a-line-dress/p/itme8ugvgq4jrqe6?pid=DREE8UGV4TPYFQH6",
          "http://www.flipkart.com/kashana-fashions-women-s-a-line-dress/p/itmea2g68x6qnnw4?pid=DREEABATS5YMYF5A",
          "http://www.flipkart.com/hugo-chavez-women-s-maxi-dress/p/itme2runhyrmhg2x?pid=DREE2RUNXZFKGGFZ",
          "http://www.flipkart.com/hugo-chavez-women-s-a-line-dress/p/itme4py5zg3jy7fp?pid=DREE4ZYTZ3KX9PUH",
          "http://www.flipkart.com/elite-collection-medium-acrylic-sticker/p/itme88knrqeg9nub?pid=STIE88KNANBFKHYM",
          "http://www.flipkart.com/kielz-women-heels/p/itmey6hqzvx9ggqp?pid=SNDEY6HQYPH8BYJ2",
          "http://www.flipkart.com/sindhi-footwear-women-wedges/p/itmdy9p9yxe4pg7z?pid=SNDDY9P9WFPBVWTF",
          "http://www.flipkart.com/kielz-women-heels/p/itmey6hqdqh6hp8y?pid=SNDEY6HQWYYVMQUG",
          "http://www.flipkart.com/belle-gambe-women-heels/p/itmdyz4xwmts2y7u?pid=SNDDYZ4XV6SZWZZY",
          "http://www.flipkart.com/kielz-women-heels/p/itmey6hq3mutcxhk?pid=SNDEY6HQXF68TNK7",
          "http://www.flipkart.com/do-bhai-women-heels/p/itmeytsbuhgyzcan?pid=SNDEYTSCGHWWHG89",
          "http://www.flipkart.com/sindhi-footwear-ballerina-bellies/p/itmdyz6rztqjq4nu?pid=SHODYZ6SYRMHDYPB",
          "http://www.flipkart.com/purple-women-heels/p/itmey8uhdcnrfvvf?pid=SNDEY8UH5TZ2AJCK",
          "http://www.flipkart.com/uberlyfe-large-vinyl-sticker/p/itme2zepqqzr9jt5?pid=STIE2ZEPACRQJKH7",
          "http://www.flipkart.com/witches-comfy-hues-women-wedges/p/itmdx969nenshghf?pid=SNDDX969ZZJJKSHB"
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "No. of clicks vs time"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "title": {
          "text": "Time"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "linecolor": "black",
         "linewidth": 1,
         "mirror": true,
         "showline": true,
         "showticklabels": false,
         "title": {
          "text": "No. of Clicks"
         }
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "scat2 = px.scatter(x=df['Time'].sort_values(ascending=True), y=df['product_url'])\n",
    "scat2.update_layout(\n",
    "    title_text='No. of clicks vs time', # title of plot\n",
    "    xaxis_title_text='Time', # xaxis label\n",
    "    yaxis_title_text='No. of Clicks', # yaxis label\n",
    "\n",
    ")\n",
    "#scat.update_xaxes(showticklabels=False)\n",
    "scat2.update_yaxes(showticklabels=False)\n",
    "scat2.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "scat2.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)\n",
    "scat2.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Data Preprocessing**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "pre_df = pd.read_csv('flipkart_com-ecommerce_sample.csv')"
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
       "(20000, 15)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.strip('[]'))\n",
    "pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.strip('\"'))\n",
    "pre_df['product_category_tree']=pre_df['product_category_tree'].map(lambda x:x.split('>>'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "#delete unwanted columns\n",
    "del_list=['crawl_timestamp','product_url','image',\"retail_price\",\"discounted_price\",\"is_FK_Advantage_product\",\"product_rating\",\"overall_rating\",\"product_specifications\"]\n",
    "pre_df=pre_df.drop(del_list,axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.corpus import stopwords \n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.stem.wordnet import WordNetLemmatizer \n",
    "lem = WordNetLemmatizer()\n",
    "import string\n",
    "stop_words = set(stopwords.words('english')) \n",
    "exclude = set(string.punctuation)\n",
    "import string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
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
       "      <th>uniq_id</th>\n",
       "      <th>product_name</th>\n",
       "      <th>product_category_tree</th>\n",
       "      <th>pid</th>\n",
       "      <th>description</th>\n",
       "      <th>brand</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>c2d766ca982eca8304150849735ffef9</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[Clothing ,  Women's Clothing ,  Lingerie, Sle...</td>\n",
       "      <td>SRTEH2FF9KEDEFGF</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>Alisha</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7f7036a6d550aaa89d34c77bd39a5e48</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed</td>\n",
       "      <td>[Furniture ,  Living Room Furniture ,  Sofa Be...</td>\n",
       "      <td>SBEEH3QGU7MFYJFY</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed (Finish Co...</td>\n",
       "      <td>FabHomeDecor</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>f449ec65dcbc041b6ae5e6a32717d01b</td>\n",
       "      <td>AW Bellies</td>\n",
       "      <td>[Footwear ,  Women's Footwear ,  Ballerinas , ...</td>\n",
       "      <td>SHOEH4GRSUBJGZXE</td>\n",
       "      <td>Key Features of AW Bellies Sandals Wedges Heel...</td>\n",
       "      <td>AW</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0973b37acd0c664e3de26e97e5571454</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[Clothing ,  Women's Clothing ,  Lingerie, Sle...</td>\n",
       "      <td>SRTEH2F6HUZMQ6SJ</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>Alisha</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>bc940ea42ee6bef5ac7cea3fb5cfbee7</td>\n",
       "      <td>Sicons All Purpose Arnica Dog Shampoo</td>\n",
       "      <td>[Pet Supplies ,  Grooming ,  Skin &amp; Coat Care ...</td>\n",
       "      <td>PSOEH3ZYDMSYARJ5</td>\n",
       "      <td>Specifications of Sicons All Purpose Arnica Do...</td>\n",
       "      <td>Sicons</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            uniq_id                           product_name  \\\n",
       "0  c2d766ca982eca8304150849735ffef9    Alisha Solid Women's Cycling Shorts   \n",
       "1  7f7036a6d550aaa89d34c77bd39a5e48    FabHomeDecor Fabric Double Sofa Bed   \n",
       "2  f449ec65dcbc041b6ae5e6a32717d01b                             AW Bellies   \n",
       "3  0973b37acd0c664e3de26e97e5571454    Alisha Solid Women's Cycling Shorts   \n",
       "4  bc940ea42ee6bef5ac7cea3fb5cfbee7  Sicons All Purpose Arnica Dog Shampoo   \n",
       "\n",
       "                               product_category_tree               pid  \\\n",
       "0  [Clothing ,  Women's Clothing ,  Lingerie, Sle...  SRTEH2FF9KEDEFGF   \n",
       "1  [Furniture ,  Living Room Furniture ,  Sofa Be...  SBEEH3QGU7MFYJFY   \n",
       "2  [Footwear ,  Women's Footwear ,  Ballerinas , ...  SHOEH4GRSUBJGZXE   \n",
       "3  [Clothing ,  Women's Clothing ,  Lingerie, Sle...  SRTEH2F6HUZMQ6SJ   \n",
       "4  [Pet Supplies ,  Grooming ,  Skin & Coat Care ...  PSOEH3ZYDMSYARJ5   \n",
       "\n",
       "                                         description         brand  \n",
       "0  Key Features of Alisha Solid Women's Cycling S...        Alisha  \n",
       "1  FabHomeDecor Fabric Double Sofa Bed (Finish Co...  FabHomeDecor  \n",
       "2  Key Features of AW Bellies Sandals Wedges Heel...            AW  \n",
       "3  Key Features of Alisha Solid Women's Cycling S...        Alisha  \n",
       "4  Specifications of Sicons All Purpose Arnica Do...        Sicons  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20000, 6)"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre_df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "uniq_id                     0\n",
       "product_name                0\n",
       "product_category_tree       0\n",
       "pid                         0\n",
       "description                 2\n",
       "brand                    5864\n",
       "dtype: int64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pre_df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(12676, 6)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "smd=pre_df.copy()\n",
    "# drop duplicate produts\n",
    "smd.drop_duplicates(subset =\"product_name\", \n",
    "                     keep = \"first\", inplace = True)\n",
    "smd.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def filter_keywords(doc):\n",
    "    doc=doc.lower()\n",
    "    stop_free = \" \".join([i for i in doc.split() if i not in stop_words])\n",
    "    punc_free = \"\".join(ch for ch in stop_free if ch not in exclude)\n",
    "    word_tokens = word_tokenize(punc_free)\n",
    "    filtered_sentence = [(lem.lemmatize(w, \"v\")) for w in word_tokens]\n",
    "    return filtered_sentence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "smd['product'] = smd['product_name'].apply(filter_keywords)\n",
    "smd['description'] = smd['description'].astype(\"str\").apply(filter_keywords)\n",
    "smd['brand'] = smd['brand'].astype(\"str\").apply(filter_keywords)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "smd[\"all_meta\"]=smd['product']+smd['brand']+ pre_df['product_category_tree']+smd['description']\n",
    "smd[\"all_meta\"] = smd[\"all_meta\"].apply(lambda x: ' '.join(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    alisha solid womens cycle short alisha Clothin...\n",
       "1    fabhomedecor fabric double sofa bed fabhomedec...\n",
       "2    aw belly aw Footwear   Women's Footwear   Ball...\n",
       "4    sicons purpose arnica dog shampoo sicons Pet S...\n",
       "5    eternal gandhi super series crystal paper weig...\n",
       "Name: all_meta, dtype: object"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "smd[\"all_meta\"].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer\n",
    "# count = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')\n",
    "# count_matrix = count.fit_transform(smd['all_meta'])\n",
    "tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')\n",
    "tfidf_matrix = tf.fit_transform(smd['all_meta'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Cosine Similarity**\n",
    "\n",
    "I will be using the Cosine Similarity to calculate a numeric quantity that denotes the similarity between two products. Since we have used the TF-IDF Vectorizer, calculating the Dot Product will directly give us the Cosine Similarity Score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics.pairwise import linear_kernel, cosine_similarity\n",
    "cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We now have a pairwise cosine similarity matrix for all the products in our dataset. The next step is to write a function that returns the most similar products based on the cosine similarity score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "smd = smd.reset_index()\n",
    "titles = smd['product_name']\n",
    "indices = pd.Series(smd.index, index=smd['product_name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_recommendations(title):\n",
    "    idx = indices[title]\n",
    "    sim_scores = list(enumerate(cosine_sim[idx]))\n",
    "    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)\n",
    "    sim_scores = sim_scores[1:31]\n",
    "    product_indices = [i[0] for i in sim_scores]\n",
    "    return titles.iloc[product_indices]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let us now try and get the top recommendations for a few products."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "rec = get_recommendations(\"FabHomeDecor Fabric Double Sofa Bed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(rec)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12219          Comfort Couch Engineered Wood 3 Seater Sofa\n",
       "12199              @home Annulus Solid Wood Dressing Table\n",
       "11866             Ethnic Handicrafts Solid Wood Single Bed\n",
       "11857              Ethnic Handicrafts Solid Wood Queen Bed\n",
       "5191                          HomeEdge Solid Wood King Bed\n",
       "12346                            Lovely Plastic Desk Chair\n",
       "11280           Stellar Engineered Wood Entertainment Unit\n",
       "6830                        Handiana Solid Wood Dining Set\n",
       "5147                     Anmol Cotton Collapsible Wardrobe\n",
       "9895                          RoyalOak Metal Outdoor Chair\n",
       "1806                   induscraft Solid Wood Computer Desk\n",
       "11079               Nilkamal CHR6020 Plastic Outdoor Chair\n",
       "5472                     Birdy Stainless Steel Collapsible\n",
       "11792                     Springwel Single Spring Mattress\n",
       "5132                      Amardeep PP Collapsible Wardrobe\n",
       "1771                     IBS Plastic Portable Laptop Table\n",
       "7469                  Varmora VCST0 Living & Bedroom Stool\n",
       "11724                     Art n Beyond Polyresin Wine Rack\n",
       "11807                       Nilkamal Queen Spring Mattress\n",
       "5125      Smart Choice Furniture Wooden Standard Shoe Rack\n",
       "6371                          COIRFIT Single Coir Mattress\n",
       "11806                        Nilkamal Double Coir Mattress\n",
       "5469            Cello Furniture Polypropylene Shoe Cabinet\n",
       "6387                 Palakz Printed Foldable Storage Stool\n",
       "11940             SRK GROUPS Aluminium, Wooden Home Temple\n",
       "1777     IBS ADJUSTABLE FOLDING KIDS MATE HOME OFFICE R...\n",
       "1785     IBS ADJUSTABLE FOLDING KIDS MATE HOME OFFICE R...\n",
       "7060                    Rrsskids Swing King Cotton Hammock\n",
       "7871                         ARRA Solid Wood 2 Seater Sofa\n",
       "12077                             Balaji Velvet Sofa Cover\n",
       "Name: product_name, dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rec"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12219          Comfort Couch Engineered Wood 3 Seater Sofa\n",
       "12199              @home Annulus Solid Wood Dressing Table\n",
       "11866             Ethnic Handicrafts Solid Wood Single Bed\n",
       "11857              Ethnic Handicrafts Solid Wood Queen Bed\n",
       "5191                          HomeEdge Solid Wood King Bed\n",
       "12346                            Lovely Plastic Desk Chair\n",
       "11280           Stellar Engineered Wood Entertainment Unit\n",
       "6830                        Handiana Solid Wood Dining Set\n",
       "5147                     Anmol Cotton Collapsible Wardrobe\n",
       "9895                          RoyalOak Metal Outdoor Chair\n",
       "1806                   induscraft Solid Wood Computer Desk\n",
       "11079               Nilkamal CHR6020 Plastic Outdoor Chair\n",
       "5472                     Birdy Stainless Steel Collapsible\n",
       "11792                     Springwel Single Spring Mattress\n",
       "5132                      Amardeep PP Collapsible Wardrobe\n",
       "1771                     IBS Plastic Portable Laptop Table\n",
       "7469                  Varmora VCST0 Living & Bedroom Stool\n",
       "11724                     Art n Beyond Polyresin Wine Rack\n",
       "11807                       Nilkamal Queen Spring Mattress\n",
       "5125      Smart Choice Furniture Wooden Standard Shoe Rack\n",
       "6371                          COIRFIT Single Coir Mattress\n",
       "11806                        Nilkamal Double Coir Mattress\n",
       "5469            Cello Furniture Polypropylene Shoe Cabinet\n",
       "6387                 Palakz Printed Foldable Storage Stool\n",
       "11940             SRK GROUPS Aluminium, Wooden Home Temple\n",
       "1777     IBS ADJUSTABLE FOLDING KIDS MATE HOME OFFICE R...\n",
       "1785     IBS ADJUSTABLE FOLDING KIDS MATE HOME OFFICE R...\n",
       "7060                    Rrsskids Swing King Cotton Hammock\n",
       "7871                         ARRA Solid Wood 2 Seater Sofa\n",
       "12077                             Balaji Velvet Sofa Cover\n",
       "Name: product_name, dtype: object"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rec"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('flipkart_com-ecommerce_sample.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
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
       "      <th>uniq_id</th>\n",
       "      <th>crawl_timestamp</th>\n",
       "      <th>product_url</th>\n",
       "      <th>product_name</th>\n",
       "      <th>product_category_tree</th>\n",
       "      <th>pid</th>\n",
       "      <th>retail_price</th>\n",
       "      <th>discounted_price</th>\n",
       "      <th>image</th>\n",
       "      <th>is_FK_Advantage_product</th>\n",
       "      <th>description</th>\n",
       "      <th>product_rating</th>\n",
       "      <th>overall_rating</th>\n",
       "      <th>brand</th>\n",
       "      <th>product_specifications</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>c2d766ca982eca8304150849735ffef9</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/alisha-solid-women-s-c...</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[\"Clothing &gt;&gt; Women's Clothing &gt;&gt; Lingerie, Sl...</td>\n",
       "      <td>SRTEH2FF9KEDEFGF</td>\n",
       "      <td>999.0</td>\n",
       "      <td>379.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/short/u/4/a/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Alisha</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7f7036a6d550aaa89d34c77bd39a5e48</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/fabhomedecor-fabric-do...</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed</td>\n",
       "      <td>[\"Furniture &gt;&gt; Living Room Furniture &gt;&gt; Sofa B...</td>\n",
       "      <td>SBEEH3QGU7MFYJFY</td>\n",
       "      <td>32157.0</td>\n",
       "      <td>22646.0</td>\n",
       "      <td>[\"http://img6a.flixcart.com/image/sofa-bed/j/f...</td>\n",
       "      <td>False</td>\n",
       "      <td>FabHomeDecor Fabric Double Sofa Bed (Finish Co...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>FabHomeDecor</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Installati...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>f449ec65dcbc041b6ae5e6a32717d01b</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/aw-bellies/p/itmeh4grg...</td>\n",
       "      <td>AW Bellies</td>\n",
       "      <td>[\"Footwear &gt;&gt; Women's Footwear &gt;&gt; Ballerinas &gt;...</td>\n",
       "      <td>SHOEH4GRSUBJGZXE</td>\n",
       "      <td>999.0</td>\n",
       "      <td>499.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/shoe/7/z/z/r...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of AW Bellies Sandals Wedges Heel...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>AW</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Ideal For\"...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0973b37acd0c664e3de26e97e5571454</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/alisha-solid-women-s-c...</td>\n",
       "      <td>Alisha Solid Women's Cycling Shorts</td>\n",
       "      <td>[\"Clothing &gt;&gt; Women's Clothing &gt;&gt; Lingerie, Sl...</td>\n",
       "      <td>SRTEH2F6HUZMQ6SJ</td>\n",
       "      <td>699.0</td>\n",
       "      <td>267.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/short/6/2/h/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Key Features of Alisha Solid Women's Cycling S...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Alisha</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Number of ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>bc940ea42ee6bef5ac7cea3fb5cfbee7</td>\n",
       "      <td>2016-03-25 22:59:23 +0000</td>\n",
       "      <td>http://www.flipkart.com/sicons-all-purpose-arn...</td>\n",
       "      <td>Sicons All Purpose Arnica Dog Shampoo</td>\n",
       "      <td>[\"Pet Supplies &gt;&gt; Grooming &gt;&gt; Skin &amp; Coat Care...</td>\n",
       "      <td>PSOEH3ZYDMSYARJ5</td>\n",
       "      <td>220.0</td>\n",
       "      <td>210.0</td>\n",
       "      <td>[\"http://img5a.flixcart.com/image/pet-shampoo/...</td>\n",
       "      <td>False</td>\n",
       "      <td>Specifications of Sicons All Purpose Arnica Do...</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>No rating available</td>\n",
       "      <td>Sicons</td>\n",
       "      <td>{\"product_specification\"=&gt;[{\"key\"=&gt;\"Pet Type\",...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                            uniq_id            crawl_timestamp  \\\n",
       "0  c2d766ca982eca8304150849735ffef9  2016-03-25 22:59:23 +0000   \n",
       "1  7f7036a6d550aaa89d34c77bd39a5e48  2016-03-25 22:59:23 +0000   \n",
       "2  f449ec65dcbc041b6ae5e6a32717d01b  2016-03-25 22:59:23 +0000   \n",
       "3  0973b37acd0c664e3de26e97e5571454  2016-03-25 22:59:23 +0000   \n",
       "4  bc940ea42ee6bef5ac7cea3fb5cfbee7  2016-03-25 22:59:23 +0000   \n",
       "\n",
       "                                         product_url  \\\n",
       "0  http://www.flipkart.com/alisha-solid-women-s-c...   \n",
       "1  http://www.flipkart.com/fabhomedecor-fabric-do...   \n",
       "2  http://www.flipkart.com/aw-bellies/p/itmeh4grg...   \n",
       "3  http://www.flipkart.com/alisha-solid-women-s-c...   \n",
       "4  http://www.flipkart.com/sicons-all-purpose-arn...   \n",
       "\n",
       "                            product_name  \\\n",
       "0    Alisha Solid Women's Cycling Shorts   \n",
       "1    FabHomeDecor Fabric Double Sofa Bed   \n",
       "2                             AW Bellies   \n",
       "3    Alisha Solid Women's Cycling Shorts   \n",
       "4  Sicons All Purpose Arnica Dog Shampoo   \n",
       "\n",
       "                               product_category_tree               pid  \\\n",
       "0  [\"Clothing >> Women's Clothing >> Lingerie, Sl...  SRTEH2FF9KEDEFGF   \n",
       "1  [\"Furniture >> Living Room Furniture >> Sofa B...  SBEEH3QGU7MFYJFY   \n",
       "2  [\"Footwear >> Women's Footwear >> Ballerinas >...  SHOEH4GRSUBJGZXE   \n",
       "3  [\"Clothing >> Women's Clothing >> Lingerie, Sl...  SRTEH2F6HUZMQ6SJ   \n",
       "4  [\"Pet Supplies >> Grooming >> Skin & Coat Care...  PSOEH3ZYDMSYARJ5   \n",
       "\n",
       "   retail_price  discounted_price  \\\n",
       "0         999.0             379.0   \n",
       "1       32157.0           22646.0   \n",
       "2         999.0             499.0   \n",
       "3         699.0             267.0   \n",
       "4         220.0             210.0   \n",
       "\n",
       "                                               image  is_FK_Advantage_product  \\\n",
       "0  [\"http://img5a.flixcart.com/image/short/u/4/a/...                    False   \n",
       "1  [\"http://img6a.flixcart.com/image/sofa-bed/j/f...                    False   \n",
       "2  [\"http://img5a.flixcart.com/image/shoe/7/z/z/r...                    False   \n",
       "3  [\"http://img5a.flixcart.com/image/short/6/2/h/...                    False   \n",
       "4  [\"http://img5a.flixcart.com/image/pet-shampoo/...                    False   \n",
       "\n",
       "                                         description       product_rating  \\\n",
       "0  Key Features of Alisha Solid Women's Cycling S...  No rating available   \n",
       "1  FabHomeDecor Fabric Double Sofa Bed (Finish Co...  No rating available   \n",
       "2  Key Features of AW Bellies Sandals Wedges Heel...  No rating available   \n",
       "3  Key Features of Alisha Solid Women's Cycling S...  No rating available   \n",
       "4  Specifications of Sicons All Purpose Arnica Do...  No rating available   \n",
       "\n",
       "        overall_rating         brand  \\\n",
       "0  No rating available        Alisha   \n",
       "1  No rating available  FabHomeDecor   \n",
       "2  No rating available            AW   \n",
       "3  No rating available        Alisha   \n",
       "4  No rating available        Sicons   \n",
       "\n",
       "                              product_specifications  \n",
       "0  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "1  {\"product_specification\"=>[{\"key\"=>\"Installati...  \n",
       "2  {\"product_specification\"=>[{\"key\"=>\"Ideal For\"...  \n",
       "3  {\"product_specification\"=>[{\"key\"=>\"Number of ...  \n",
       "4  {\"product_specification\"=>[{\"key\"=>\"Pet Type\",...  "
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['uniq_id', 'crawl_timestamp', 'product_url', 'product_name',\n",
       "       'product_category_tree', 'pid', 'retail_price', 'discounted_price',\n",
       "       'image', 'is_FK_Advantage_product', 'description', 'product_rating',\n",
       "       'overall_rating', 'brand', 'product_specifications'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "le = LabelEncoder()\n",
    "data = data.apply(LabelEncoder().fit_transform)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 20000 entries, 0 to 19999\n",
      "Data columns (total 15 columns):\n",
      " #   Column                   Non-Null Count  Dtype\n",
      "---  ------                   --------------  -----\n",
      " 0   uniq_id                  20000 non-null  int32\n",
      " 1   crawl_timestamp          20000 non-null  int32\n",
      " 2   product_url              20000 non-null  int32\n",
      " 3   product_name             20000 non-null  int32\n",
      " 4   product_category_tree    20000 non-null  int32\n",
      " 5   pid                      20000 non-null  int32\n",
      " 6   retail_price             20000 non-null  int64\n",
      " 7   discounted_price         20000 non-null  int64\n",
      " 8   image                    20000 non-null  int32\n",
      " 9   is_FK_Advantage_product  20000 non-null  int64\n",
      " 10  description              20000 non-null  int32\n",
      " 11  product_rating           20000 non-null  int32\n",
      " 12  overall_rating           20000 non-null  int32\n",
      " 13  brand                    20000 non-null  int32\n",
      " 14  product_specifications   20000 non-null  int32\n",
      "dtypes: int32(12), int64(3)\n",
      "memory usage: 1.4 MB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "# data = data.drop(['crawl_timestamp'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.cluster import KMeans \n",
    "from sklearn.metrics import silhouette_score\n",
    "from sklearn.preprocessing import MinMaxScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Finding the optimum number of clusters for k-means classification\n",
    "from sklearn.cluster import KMeans\n",
    "wcss = []\n",
    "\n",
    "for i in range(1, 11):\n",
    "    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)\n",
    "    kmeans.fit(data)\n",
    "    wcss.append(kmeans.inertia_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEWCAYAAABrDZDcAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAq70lEQVR4nO3deXxV9Z3/8dcnKyRAICRAIEACiICALAFEcUWrtY611drNHWvbsVrb6bS1M9PFme6dtnY6v5laEbFq1YKOVm3dN0CBBJFdZQkQFhMg7JCQ5PP74xzgGkMSIDcnyX0/H4/7yLnnnHvO517lvu/3+z2LuTsiIpK4kqIuQEREoqUgEBFJcAoCEZEEpyAQEUlwCgIRkQSnIBARSXAKAmlTzOyHZvZgK+znPDMri3leamYXxnu/rcXMbjCzOS20rQ99VtLxpERdgCQWM9sb8zQDqAJqw+dfbv2K2j8zKwDWAanuXhNxOdIOqUUgrcrduxx+ABuAf4iZ91DU9YkkIgWBtEVpZvaAme0xs+VmVnR4gZn1NbPZZlZhZuvM7PZjbcTM0s3sV2a2wcw+MLP/NbPOjex3gpmtMLNKM5thZp1itvUlM1ttZjvM7Ckz6xvO/5GZ/Vc4nWpm+8zsl+HzzmZ20MyyG6jtPDMrM7Nvm1m5mW0xsyvM7FIzey/cz/di1k8ys++a2Roz225mj8Vs9/Xw704z22tmk2Ne96vw/awzs4/X+xyfCvez2sy+FLOss5ndH75uBTChkc9MOgAFgbRFlwOPAN2Bp4DfQ/BlCPwVeAfoB0wF7jCzi4+xnZ8BQ4ExwJDwNd9vZL9fBC4GBoev+9dwvxcAPwWuBvKA9WF9AK8B54XTE4CtwDnh88nAu+6+4xj76wN0iqnrj8A1wHjgbODfzKwwXPc24ArgXKAvUAn8d7js8P66hy2rN8Pnk4B3gRzgF8B0M7Nw2SNAWbitq4CfhO8T4AfhZzA4/DyuP0b90lG4e7t7APcB5cCyZqx7DrAIqAGuipk/BngTWA4sAT4b9ftKtAdQClxYb94PgRdjno8ADoTTk4AN9da/E5jRwLYN2AcMjpk3GVgXTp8HlNWr5Ssxzy8F1oTT04FfxCzrAhwCCoDOwEGgJ/Bd4HsEX7BdgB8BvzvGez8POAAkh8+7Ag5MilmnBLginF4JTI1ZlhfWkBLW4UBKzPIbgNUxzzPCdfoA/QnGZbrGLP8pcH84vRa4JGbZLbGflR4d79FeB4vvJ/iV+EAz1t1A8I/iW/Xm7weuc/f3w2Z+iZk95+47W7BOOTFbY6b3A53MLAUYCPQ1s50xy5OBNxrYRi7Bl1/J0R/BWLj+sWyMmV5P8GuZ8O+iwwvcfa+ZbQf6uXupmRUT/FI/B/gxwY+Ms8J5/9XI/ra7++GB8gPh3w9ilh8gCBQI3vsTZlYXs7wW6N3I9o98ju6+P/wcuhCE1g5331Pv/R7uguvLRz8L6cDaZRC4++vhkRJHmNlggqZyLsGXx5fcfZW7l4bL6+pt472Y6c1mVh6+dmdci5eTsZHgF/0pzVh3G8EX6WnuvqmZ2+8fMz0A2BxObyb4IgbAzDIJvkwPb/c14AJgLLAwfH4xMJGj/fcnayNwk7vPrb/AzAY2sH5jNgPZZtY1JgwGcPT9bCH4LJbHLJMOrCONEdwD3Obu4wl+/f+/5r7QzCYCacCaONUmLWMBsMfMvhMOaCab2Ugz+8hgprvXEfS5/8bMegGYWb9GxhMAbjWz/HAQ9l+AR8P5fwZuNLMxZpYO/ASYf/hHBsEX/3XACnevBl4FbiYIrYqTfdOh/wV+fPhL38xyzeyT4bIKoA4Y1JwNuftGYB7wUzPrZGajgWnA4fM3HgPuNLMeZpZPMD4hHViHCAIz6wKcCfzFzBYDfyDoQ23Oa/OAPwE3hl8e0kaF3SiXEXS9rCP41X8vkHWMl3wHWA28ZWa7gReBUxvZxcPA8wR95GuA/wj3+yLwb8Bsgl/Lg4HPxbxuHsFYweFf/ysIxg1aqjUAcDfBwPnzZrYHeItgzAR330/QJTXXzHaa2RnN2N7nCcYWNgNPAD8I3ycEYxvrCT7j5wn+fUgHZu7t88Y0YdfQ0+4+0sy6ERydccwvfzO7P1x/Vsy8bgS/3n4SO19EJJF0iBaBu+8G1pnZZwAscHpjrzGzNIJfQg8oBEQkkbXLFoGZ/Zng8LscgqMsfgC8DPwPQZdQKvCIu98V9h8/AfQgaK5vdffTzOwaYAZHB8QAbnD3xa31PkRE2oJ2GQQiItJyOkTXkIiInLh2dx5BTk6OFxQURF2GiEi7UlJSss3dcxta1u6CoKCggOLi4qjLEBFpV8zsmGeIq2tIRCTBKQhERBKcgkBEJMEpCEREEpyCQEQkwSkIREQSnIJARCTBJUwQrKnYy4/+upxDtbrStIhIrIQJgvXb9zFjbinPLt0SdSkiIm1KwgTBeUN7MSg3k+lz1qEL7YmIHJUwQZCUZNx4ViFLynZRvL4y6nJERNqMuAdBeF/Zt83s6QaWpZvZo2a22szm178hfUu7clw/sjqnMv2NdfHcjYhIu9IaLYKvAyuPsWwaUOnuQ4DfAD+PZyEZaSl8YdIAnl+xlY079sdzVyIi7UZcg8DM8oFPENxgvCGfBGaG07OAqWZm8azp+skFJJkxY25pPHcjItJuxLtF8Fvg28CxjtnsB2wEcPcaYBfQs/5KZnaLmRWbWXFFRcVJFdQnqxOfGJ3HY8Ub2XPw0EltS0SkI4hbEJjZZUC5u5ec7Lbc/R53L3L3otzcBu+rcFymTSlkb1UNjy7ceNLbEhFp7+LZIjgLuNzMSoFHgAvM7MF662wC+gOYWQqQBWyPY00AjM7vzoSCHtw/r5TaOh1KKiKJLW5B4O53unu+uxcAnwNedvdr6q32FHB9OH1VuE6rfDNPm1JIWeUBnl++tTV2JyLSZrX6eQRmdpeZXR4+nQ70NLPVwDeB77ZWHReN6EP/7M7cN1eHkopIYmuVexa7+6vAq+H092PmHwQ+0xo11JecZNxwZiH//vQKlpTtZHR+9yjKEBGJXMKcWdyQq4vy6ZKewvQ5ahWISOJK6CDo2imVz07ozzNLtrB118GoyxERiURCBwHADWcWUOfOzDdLoy5FRCQSCR8E/bMzuPi0Pjw8fwP7q2uiLkdEpNUlfBBAcCjprgOHmL1oU9SliIi0OgUBMH5gD07Pz2LGnHXU6QQzEUkwCgLAzLhpSiFrt+3j1ffKoy5HRKRVKQhCl47KIy+rkw4lFZGEoyAIpSYncd3kAuau3s7KLbujLkdEpNUoCGJ8YeIAOqcmc59aBSKSQBQEMbIyUrlqfD5PLt5MxZ6qqMsREWkVCoJ6bjyrgOraOh58a33UpYiItAoFQT2DcrswdVgvHnxrPQcP1UZdjohI3CkIGjBtSiHb91Xz1OLNUZciIhJ3CoIGTB7ck2F9unLf3HW00n1yREQioyBogJkxbUohq7buYe7quN85U0QkUgqCY7h8TF9yuqQzfc7aqEsREYkrBcExpKckc+0ZA3nl3QpWl++NuhwRkbhREDTii2cMIC0liRm6r7GIdGAKgkbkdEnnU2P6MXtRGZX7qqMuR0QkLhQETbhxSgEHD9Xx8IINUZciIhIXCoImDOvTjSlDcnjgzVKqa+qiLkdEpMUpCJph2pRCPthdxbNLt0RdiohIi1MQNMO5Q3MZlJvJ9Dk6wUxEOh4FQTMkJRk3nVXI0k27WFhaGXU5IiItSkHQTFeOy6d7RqpOMBORDkdB0Eyd05L5wsQBPL/iAzZs3x91OSIiLUZBcByum1xAshkz5ukEMxHpOBQEx6FPVicuG53HYws3svvgoajLERFpEQqC4zRtyiD2Vdfy2MKNUZciItIiFATHaVR+FhMLspkxt5SaWp1gJiLtn4LgBNw0pZBNOw/w/IoPoi5FROSkKQhOwEUjejMgO4PpczRoLCLtX9yCwMw6mdkCM3vHzJab2Y8aWOcGM6sws8Xh4+Z41dOSkpOMG84soGR9JYs37oy6HBGRkxLPFkEVcIG7nw6MAS4xszMaWO9Rdx8TPu6NYz0t6uoJ/emansJ9ahWISDsXtyDwwOFbe6WGjw5zoZ4u6Sl8dkJ/nl26hS27DkRdjojICYvrGIGZJZvZYqAceMHd5zew2pVmtsTMZplZ/2Ns5xYzKzaz4oqKiniWfFyuP7OAOndmzlsfdSkiIicsrkHg7rXuPgbIByaa2ch6q/wVKHD30cALwMxjbOcedy9y96Lc3Nx4lnxc+mdncMnIPvx5wQb2V9dEXY6IyAlplaOG3H0n8ApwSb352929Knx6LzC+NeppSdOmFLLrwCFml5RFXYqIyAmJ51FDuWbWPZzuDFwErKq3Tl7M08uBlfGqJ17GDejB6f27c9/cUurqOswQiIgkkHi2CPKAV8xsCbCQYIzgaTO7y8wuD9e5PTy09B3gduCGONYTF2bGtCmFrNu2j1feLY+6HBGR45YSrw27+xJgbAPzvx8zfSdwZ7xqaC0fH9mHvKxOTJ+zjqnDe0ddjojIcdGZxS0gNTmJ688sYN6a7azYvDvqckREjouCoIV8fsIAOqcmc99cnWAmIu2LgqCFZGWk8pmifJ5avJnyPQejLkdEpNkUBC3oxrMKOVRXx4NvbYi6FBGRZlMQtKDCnEymDuvFQ2+t5+Ch2qjLERFpFgVBC7tpSiHb91Xz5OJNUZciItIsCoIWNnlQT4bndWP6nHW46wQzEWn7FAQt7PAJZu99sJc5q7dFXY6ISJMUBHHwD6fnkdMlXXcwE5F2QUEQB+kpyVw3eSCvvlvB6vI9UZcjItIoBUGcfHHSANJSkrhvbmnUpYiINEpBECc9u6Tz6bH9eHxRGZX7qqMuR0TkmBQEcXTTlEIOHqrj4QU6wUxE2i4FQRwN7d2Vs0/JYea8Uqpr6qIuR0SkQQqCOLtpSiHle6p4ZunmqEsREWmQgiDOzj0ll8G5mTrBTETaLAVBnCUlGTdNKWTZpt0sWLcj6nJERD5CQdAKPj02n+4ZqTrBTETaJAVBK+iclswXJw3ghZUfsH77vqjLERH5EAVBK7lucgEpScYMnWAmIm2MgqCV9O7WictG9+UvxRvZffBQ1OWIiByhIGhF06YUsq+6lkcXbIy6FBGRIxQErWhkvywmFmZz39x17DqgVoGItA0Kglb2nUtOZdveKr728CJqanW2sYhET0HQysYPzObHV4zijfe3cdfTK6IuR0SElKgLSERXT+jPmoq9/OH1tQzO7cL1ZxZEXZKIJDAFQUS+fckw1lTs40d/XU5BTibnDs2NuiQRSVDqGopIcpJx9+fGcGqfbnztoUW8/4HuZCYi0VAQRCgzPYV7ry8iPTWZaTOL2aEb2IhIBBQEEevXvTN/vG48W3cf5Ct/KqGqpjbqkkQkwSgI2oCxA3rwq8+czoLSHXzv8WW6XLWItCoNFrcRl5/elzXle7n7pfcZ0qsLXz1vcNQliUiCUBC0IXdceAprt+3jF8+tYlBuJhef1ifqkkQkAahrqA0xM3551WhOz+/OHY8sZtmmXVGXJCIJoNEgMLMJZtYn5vl1Zvakmf3OzLKbeG0nM1tgZu+Y2XIz+1ED66Sb2aNmttrM5ptZwQm/kw6iU2oy91w3nh4ZqXzpgWLKdx+MuiQR6eCaahH8AagGMLNzgJ8BDwC7gHuaeG0VcIG7nw6MAS4xszPqrTMNqHT3IcBvgJ8fV/UdVK+unbj3+gnsOnCILz1QzMFDOpJIROKnqSBIdvfDN9r9LHCPu892938DhjT2Qg/sDZ+mho/6h8N8EpgZTs8CppqZNbv6DmxE327c/bmxLNm0i3967B3q6nQkkYjER5NBYGaHB5SnAi/HLGtyoNnMks1sMVAOvODu8+ut0g/YCODuNQQtjZ4NbOcWMys2s+KKioqmdtthXDSiN9+9ZBjPLN3Cb198L+pyRKSDaioI/gy8ZmZPAgeANwDMbAjBl3aj3L3W3ccA+cBEMxt5IkW6+z3uXuTuRbm5iXVNnlvOGcRnxufzu5dX8+TiTVGXIyIdUKO/6t39x2b2EpAHPO9Hz3RKAm5r7k7cfaeZvQJcAiyLWbQJ6A+UhS2PLGD7cdTf4ZkZP/7UKNbv2M8/z1pCfo8Mxg/sEXVZItKBNHXUUAZQ4u5PuPs+MzvVzL4BjHT3RU28NtfMuofTnYGLgFX1VnsKuD6cvgp42XVa7UekpSTxh2vGk5fViS//qZiyyv1RlyQiHUhTXUN/BwrgSHfQm8Ag4FYz+2kTr80DXjGzJcBCgjGCp83sLjO7PFxnOtDTzFYD3wS+e2Jvo+PrkZnG9OsnUFVTx80zi9lbVRN1SSLSQVhjP8DNbKm7jwqn/x3IdvdbzSyNoKUwqpXqPKKoqMiLi4tbe7dtxhvvV3DDjIWcNzSXe64rIjlJB1mJSNPMrMTdixpa1lSLIDYlLgBeAHD3akA33I3A2afk8sN/GMFLq8r56bMroy5HRDqApg4BXWJmvyIY1B0CPA9wuO9fonHt5AJWl+/l3jnrGNKrC5+bOCDqkkSkHWuqRfAlYBvBOMHH3P3wKOUI4FdxrEua8G+XjeCcobn86/8tY96abVGXIyLtWFNB0AX4q7t/3d3fiZm/i2AgWSKSkpzE778wlsKcTL764CLWbdsXdUki0k41FQT/RQNn+gLZwN0tX44cj26dUpl+/QSSk4xp9y9k1/5DUZckIu1QU0EwxN1frz/T3d8ARsenJDkeA3pm8L/XjGdj5X7+8eESDtVqDF9Ejk9TQdC1kWWpLVmInLiJhdn89NOjmbt6Oz94arludSkix6WpIFhtZpfWn2lmHwfWxqckORFXjc/nK+cO5uH5G5gxtzTqckSkHWnq8NE7gGfM7GqgJJxXBEwGLotjXXICvn3xqayt2Mt/PLOCwtxMzj+1V9QliUg70FSL4BPANcBcYGD4eA0Y7e66LnIbk5Rk/OazYxjWpxu3Pfw2727dE3VJItIONBUE+cBvgV8AEwjuVlYOZMS3LDlRmekpTL+hiIy0ZKbNXMi2vVVRlyQibVyjQeDu33L3M4HewJ3ADuBGYJmZrWiF+uQE5GV15o/XFVGxp4ov/6lEt7oUkUY11SI4rDPQjeB+AVnAZqD+3cakDTm9f3d+ffUYStZXcufjS3UkkYgcU6ODxWZ2D3AasIfgi38e8Gt3r2yF2uQkfWJ0HmsqhvLrF95jSK8u3Hp+o7eZFpEE1dRRQwOAdOB9ggvPlQE741yTtKDbLhjCmoq9/PK5dxmUk8nHR+VFXZKItDFN3aryEjMzglbBmcA/ASPNbAfwprv/oBVqlJNgZvz8ytFs2LGfbzy2mPweGYzKz4q6LBFpQ5ocI/DAMuBZ4G8Eh5IOBr4e59qkhXRKTeaea4vomZnOzQ8sZOuug1GXJCJtSFP3LL7dzB4xsw0E5w9cRnDf4U8TXHhO2oncrunce30Rew/WcPMDC9lfrVtdikigqRZBAfAXYJK7D3b3a939f9z9HXfX1c3ameF53fjd58eyfPNuvvnoO9TV6UgiEWn6PIJvuvtsd9/SWgVJfE0d3pt/uXQ4f1++lbueXkF1jfJcJNE1ddSQdEDTphRSVnmA++eV8tba7fzqM6czsp8GkEUSVXNPKJMOxMz44eWncc+149m+r5pP/vdcfvXcu1TV6AxkkUSkIEhgHzutDy9+41yuGNOP37+ymst+N4e3N+hcQZFEoyBIcFkZqfzn1acz44YJ7K2q4cr/mcdPnl2p6xOJJBAFgQBw/rBePPeNc/jshP7c8/paPn73Gyws3RF1WSLSChQEckS3Tqn89NOjeXDaJA7V1nH1H97kh08t1zkHIh2cgkA+YsopOTx3xzlce8ZA7p9XysW/fZ15a7ZFXZaIxImCQBqUmZ7CXZ8cyaO3nEGSGV/443z+5Yml7Dl4KOrSRKSFKQikUZMG9eTvXz+Hm6cU8vCCDVz8m9d57b2KqMsSkRakIJAmdU5L5l8vG8Gsr5xJ57Rkrr9vAd+e9Q67Dqh1INIRKAik2cYP7MEzt5/NV88bzOxFm/jYb17jpZUfRF2WiJwkBYEcl06pyXznkmE88Y9n0r1zGtNmFnPHI29Tua866tJE5AQpCOSEjM7vzl9vm8LtU0/h6SVbuOg3r/G3pbo2oUh7FLcgMLP+ZvaKma0ws+Vm9pEb2ZjZeWa2y8wWh4/vx6seaXlpKUl886KhPPW1KfTu1omvPrSIf3yohG17q6IuTUSOQzxbBDXAP7n7COAM4FYzG9HAem+4+5jwcVcc65E4GdG3G/9361n888Wn8uKKci769Ws8uXgT7rrfgUh7ELcgcPct7r4onN4DrAT6xWt/Eq3U5CRuPX8IT98+hQE9M/n6I4u55U8llO/WbTFF2rpWGSMwswJgLDC/gcWTzewdM/ubmZ12jNffYmbFZlZcUaFj2Nuyob27Mvsrk/nepcN4/b0KLvz1a/yleKNaByJtmMX7H6iZdSG43/GP3f3xesu6AXXuvtfMLgXudvdTGtteUVGRFxcXx69gaTFrK/by7VlLKF5fyXmn5vKTT42ib/fOUZclkpDMrMTdixpaFtcWgZmlArOBh+qHAIC773b3veH0s0CqmeXEsyZpPYNyu/DYlyfzg38Ywfy1O/jYb17nzws2qHUg0sbE86ghA6YDK93918dYp0+4HmY2Maxne7xqktaXlGTceFYhz91xDqP6ZXHn40u5Zvp8Nu7YH3VpIhKKZ4vgLOBa4IKYw0MvNbOvmNlXwnWuApaZ2TvA74DPuX4udkgDembw0M2T+I8rRrJ4w04u/u3rzJxXSl2d/nOLRC3uYwQtTWME7d+mnQf47uwlvPH+NiYWZPPvV4zk1D5doy5LpEOLbIxApCH9unfmgZsm8ourRrNy624u/u3rXHffAl5/r0LjByIRUItAIrVjXzUPvbWemW+uZ9veKob27sLNUwZx+Zi+dEpNjro8kQ6jsRaBgkDahKqaWp5avJnpc9axausecrqkcc0ZA7nmjIHkdEmPujyRdk9BIO2GuzNvzXbufWMtr7xbQVpKEp8a049pZxcytLfGEUROVGNBkNLaxYg0xsw4a0gOZw3JYXX5Xu6bu47ZJWU8WryRc4bmMm1KIeeckkN41LGItAC1CKTN27GvmofnB+MIFXuCcYRpUwr55Jh+GkcQaSZ1DUmHUFVTy1/f2cL0OetYuWU3PTOPjiPkdtU4gkhjFATSobg7b67Zzr1z1vHyqnLSUpK4Ykxfpk0ZpPMRRI5BYwTSoZgZZw7J4cxwHGHG3HXMXlTGY8VlnH1KDtOmFHLu0FyNI4g0k1oE0iFU7qvm4QUbuH9eKRV7qjilVzCOcMVYjSOIgLqGJIFU1dTydDiOsGLLbrLDcYRrNY4gCU5BIAnH3Xlz7Xamv7GOl1aVk5acxBVjNY4giUtjBJJwzIwzB+dw5uAc1lQE4wizSjSOINIQtQgkYRweR5g5r5TyPVUMCccRPqVxBEkA6hoSiVFdU8fTSzZz7xsx4wiTBvD5SQPIy9KtNKVjUhCINMDdeWvtDqbPWcuLK8sxgylDcrhqfD4fG9GHzmlqJUjHoTECkQaYGZMH92Ty4J6s376P2Ys2MbukjK8/spiu6SlcdnoeV43PZ9yAHhpLkA5NLQKRGHV1zlvrtjOrpIy/Ld3KgUO1FOZkcuW4fnxqXD79uqvrSNondQ2JnIC9VTX8bekWZpWUMX/dDszgrME5XDm+H5eclqeuI2lXFAQiJ2nD9v3MXlTG7EVllFUeoEt6Cp8YlcdVRfkUDVTXkbR9CgKRFlJX5ywo3cGskjKeXbqF/dW1DOyZwVXj8vnUuH7k98iIukSRBikIROJgX1UNf1u2ldklZby5djsAZw7uyVXj87lkZB8y0nQshrQdCgKRONu4Yz+PL9rE7EVlbNixn8y0ZC4dFRx1NLEwW11HEjkFgUgrcXcWllYyq2QjzyzZwr7qWgZkZ3DluHw+Pa4f/bPVdSTRUBCIRGB/dQ1/X7aV2YvKmLdmO+5wxqBsrhrfn4+P7ENmurqOpPUoCEQiVla5nycWbWLWojLWb99PRmzXUUE2SUnqOpL4UhCItBHuTsn6SmaVlPH0ki3sraohv0dnrhyXz5Xj8hnQU11HEh8KApE26EB1Lc8t38qskjLmrtmGO0wszOaS0/owdXgvBvbMjLpE6UAUBCJt3OadB3ji7U3839ubeL98LwBDenVh6rBeTB3em3EDupOSnBRxldKeKQhE2pH12/fx0spyXl5Vzvx12zlU63TPSOW8oblcMLw35w7NJatzatRlSjujIBBpp/YcPMQb72/jxZUf8Oq7FezYV01ykjGhoAcXDu/NBcN6MSi3S9RlSjugIBDpAGrrnMUbK3lpZTkvrSzn3Q/2ADAoJ5Opw3txwbDeFBX0IFVdSNIABYFIB7Rxx35eXlXOiys/YP7aHVTX1tGtUwrnntqLC4f34tyhuXTPSIu6TGkjIgkCM+sPPAD0Bhy4x93vrreOAXcDlwL7gRvcfVFj21UQiHzU3qoa5rxfwUsry3nl3XK27Q26kMYP7HFkwHlwbqYudZHAogqCPCDP3ReZWVegBLjC3VfErHMpcBtBEEwC7nb3SY1tV0Eg0ri6Ouedsp1BF9KqclZu2Q3AwJ4ZTB3Wm6nDezGhIJu0FHUhJZI20TVkZk8Cv3f3F2Lm/QF41d3/HD5/FzjP3bccazsKApHjs2nnAV5eVc5LKz9g3prtVNfU0TU9hXOG5jJ1eC/OO7UX2ZnqQuroIr9nsZkVAGOB+fUW9QM2xjwvC+d9KAjM7BbgFoABAwbErU6Rjqhf985ce8ZArj1jIPura5jz/rYgGFaV88zSLSQZjBvQgwuG9+LC4b05pVcXdSElmLi3CMysC/Aa8GN3f7zesqeBn7n7nPD5S8B33P2YP/nVIhBpGXV1zrLNu3hxZdBaWL456ELqn92Z808Nuo+KCnqQl6X7NHcEkbUIzCwVmA08VD8EQpuA/jHP88N5IhJnSUnG6PzujM7vzjcvGsrWXQd5adUHvLyynL8Ul/HAm+uBoEVRVNCDooE9KCrIZmjvriTrInkdSjwHiw2YCexw9zuOsc4ngK9xdLD4d+4+sbHtqkUgEn+HautYsXk3xesrKVm/g+LSSsr3VAHQNT2FsQPDYBjYgzEDuutubO1AVEcNTQHeAJYCdeHs7wEDANz9f8Ow+D1wCcHhozc21i0ECgKRKLg7G3ccoHj9jiAcSiuPnNCWnGSc1rcb4wf2oGhg0J3Uu1uniCuW+trEUUMtRUEg0jbs2n+IRRsqg3AorWTxxp1U1QS/+fpnd6ZoYHYQDgU9GNqrq+65ELHIjxoSkY4nKyOV84f14vxhvQCorqlj+eZdlKyvpLi0kjfe38YTbwdDft06pTAu7EoaPzCbMf270zktOcryJYaCQERaRFpKEmMH9GDsgB7cfHbQnbR++/4PjTO8+m4FAClJxmn9so6MM4wv6EGvrupOioq6hkSk1ezcXx20GMJxhsVlO6kOu5MG9sz40DjDkNwu6k5qQRojEJE2qaqmlmWbdh9pMZSsr2T7vmoAsjqnMnZAd0b1y2JkvyxG9csiL6uTTnY7QQoCEWkX3J112/YdbTFs3Mn75XuoC7+memamHQmFkf26MbJfFv26d1Y4NIMGi0WkXTAzBuV2YVBuF64uCs41PVBdy4otu1m2aRdLN+1i2aZdzFm9jdowHbIz0zitbzdGHQmILPJ7KByOh4JARNq0zmnJjB/Yg/EDexyZd/BQLStjwmHppt3c8/paasJw6JGRysiYLqVRCodGKQhEpN3plJp85Ailww4eqmXV1j1Bq6FsF8s27+KPMeGQ1Tn1SHfS4XAYkJ2hcEBBICIdRKfUZMb0786Y/t2PzKuqqeXdw+EQth7um7OOQ7VBOHTrlBIz5hD8Hdgz8cJBQSAiHVZ6SvKRC+sdVlVTy3tb94ZdSrtYvnkXM+aWUl0bHMbatVPKkTGHw+FQ0DOzQx/KqiAQkYSSnpLMqPwsRuVnHZlXXVPHex/s+dCA9Mw31x85xyEzLZlhed0YnteV4XndGNanG8P6dCUzvWN8herwURGRBhyqPRoOKzbvZuWWPazcups9B2sAMIOB2RkMz+sW8+jaZg9n1eGjIiLHKTU5idP6ZnFa36MtB3enrPIAK7eEwbBlNyu37OZvy7YeWadbpxSG5XVjREwLYmjvrnRKbbvXVlIQiIg0k5nRPzuD/tkZfOy0Pkfm76uqYdXWo8GwcstuHiveyP7qWgCSDAbldjnSahgeBkWvrultovWgIBAROUmZ6SkfOdehrs7ZsGP/kWBYsWUPi9ZX8td3Nh9ZJzszjWF9un6oa+mUXl1JS0lq1foVBCIicZCUZBTkZFKQk8nHR+Udmb/rwCFWHWk5BOMOD761/si9HFKSjCG9Ptx6GJ7XjZwu6XGrVUEgItKKsjqnMmlQTyYN6nlkXk1tHaXb97EiZtxh3pqj93MAyO2azi1nD+JL5wxq8ZoUBCIiEUtJTmJIr64M6dWVy0/ve2T+jn3VMV1Lu+nVLT6tAgWBiEgblZ2ZxllDcjhrSE5c99O6IxIiItLmKAhERBKcgkBEJMEpCEREEpyCQEQkwSkIREQSnIJARCTBKQhERBJcu7sfgZlVAOujruMk5QDboi6iDdHn8WH6PI7SZ/FhJ/N5DHT33IYWtLsg6AjMrPhYN4hIRPo8Pkyfx1H6LD4sXp+HuoZERBKcgkBEJMEpCKJxT9QFtDH6PD5Mn8dR+iw+LC6fh8YIREQSnFoEIiIJTkEgIpLgFAStyMz6m9krZrbCzJab2dejrilqZpZsZm+b2dNR1xI1M+tuZrPMbJWZrTSzyVHXFCUz+0b472SZmf3ZzDpFXVNrMrP7zKzczJbFzMs2sxfM7P3wb4+W2JeCoHXVAP/k7iOAM4BbzWxExDVF7evAyqiLaCPuBv7u7sOA00ngz8XM+gG3A0XuPhJIBj4XbVWt7n7gknrzvgu85O6nAC+Fz0+agqAVufsWd18UTu8h+IfeL9qqomNm+cAngHujriVqZpYFnANMB3D3anffGWlR0UsBOptZCpABbI64nlbl7q8DO+rN/iQwM5yeCVzREvtSEETEzAqAscD8iEuJ0m+BbwN1EdfRFhQCFcCMsKvsXjPLjLqoqLj7JuBXwAZgC7DL3Z+Ptqo2obe7bwmntwK9W2KjCoIImFkXYDZwh7vvjrqeKJjZZUC5u5dEXUsbkQKMA/7H3ccC+2ihZn97FPZ9f5IgIPsCmWZ2TbRVtS0eHPvfIsf/KwhamZmlEoTAQ+7+eNT1ROgs4HIzKwUeAS4wswejLSlSZUCZux9uIc4iCIZEdSGwzt0r3P0Q8DhwZsQ1tQUfmFkeQPi3vCU2qiBoRWZmBH3AK93911HXEyV3v9Pd8929gGAQ8GV3T9hffO6+FdhoZqeGs6YCKyIsKWobgDPMLCP8dzOVBB48j/EUcH04fT3wZEtsVEHQus4CriX49bs4fFwadVHSZtwGPGRmS4AxwE+iLSc6YctoFrAIWErwXZVQl5swsz8DbwKnmlmZmU0DfgZcZGbvE7SaftYi+9IlJkREEptaBCIiCU5BICKS4BQEIiIJTkEgIpLgFAQiIglOQSBtjpm5mf1nzPNvmdkPW2jb95vZVS2xrSb285nwCqKvxLMuMyswsy8cf4UiRykIpC2qAj5tZjlRFxIrvPhZc00DvuTu58ernlABcFxBcJzvQxKAgkDaohqCk4e+UX9B/V/OZrY3/Huemb1mZk+a2Voz+5mZfdHMFpjZUjMbHLOZC82s2MzeC695dPi+CL80s4VmtsTMvhyz3TfM7CkaONPXzD4fbn+Zmf08nPd9YAow3cx+2cBrvhO+5h0z+8gJQWZWejgEzazIzF4Np8+NORHxbTPrSnBC0dnhvG80932YWaaZPRPWsMzMPtuc/zDSMemXgbRV/w0sMbNfHMdrTgeGE1y6dy1wr7tPtOAGQLcBd4TrFQATgcHAK2Y2BLiO4AqXE8wsHZhrZoevdjkOGOnu62J3ZmZ9gZ8D44FK4Hkzu8Ld7zKzC4BvuXtxvdd8nOBiapPcfb+ZZR/H+/sWcKu7zw0vXHiQ4MJ033L3w4F2S3Peh5ldCWx290+Er8s6jjqkg1GLQNqk8KqsDxDcnKS5Fob3fKgC1gCHvwCXEnz5H/aYu9e5+/sEgTEM+BhwnZktJrg0eE/glHD9BfVDIDQBeDW8MFoN8BDBPQUacyEww933h++z/vXmGzMX+LWZ3Q50D/dZX3Pfx1KCSxX83MzOdvddx1GHdDAKAmnLfkvQ1x57Xf4awv9vzSwJSItZVhUzXRfzvI4Pt37rX1fFAQNuc/cx4aMw5vr3+07mTZyAI+8ROHJ7Rnf/GXAz0Jngl/6wBl7brPfh7u8RtBCWAv8RdmdJglIQSJsV/lp+jCAMDisl6IoBuBxIPYFNf8bMksJxg0HAu8BzwFfDy4RjZkOt6RvDLADONbMcM0sGPg+81sRrXgBuNLOMcD8NdQ2VcvQ9Xnl4ppkNdvel7v5zYCFBS2YP0DXmtc16H2G31n53fxD4JYl9yeuEpzECaev+E/hazPM/Ak+a2TvA3zmxX+sbCL7EuwFfcfeDZnYvQffRIjMzgruFXdHYRtx9i5l9F3iF4Jf4M+7e6GWB3f3vZjYGKDazauBZ4Hv1VvsRwUDzvwOvxsy/w8zOJ2jhLAf+Fk7Xhp/H/QT3PW7O+xgF/NLM6oBDwFcbq1s6Nl19VEQkwalrSEQkwSkIREQSnIJARCTBKQhERBKcgkBEJMEpCEREEpyCQEQkwf1/ERUDE6JYBQIAAAAASUVORK5CYII=",
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
    "import matplotlib.pyplot as plt\n",
    "plt.plot(range(1, 11), wcss)\n",
    "plt.title('The elbow method')\n",
    "plt.xlabel('Number of clusters')\n",
    "plt.ylabel('WCSS') #within cluster sum of squares\n",
    "plt.show()"
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
   "display_name": "Python 3.6.8 64-bit",
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
   "version": "3.6.8"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "f4e9cda46bb2d9d7fe6ecdff0f8336a934348bf06cb492f2f42f60739b3403b4"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
