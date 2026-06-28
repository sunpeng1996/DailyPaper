---
title: Data-Driven Duration Management -- Term Structure Forecasting Using Machine
  Learning
title_zh: Data-Driven Duration Management -- Term Structure
authors:
- Tobias Lausser
- Joao Eduardo Vuolo
- Rudi Zagst
arxiv_id: '2606.26815'
url: https://arxiv.org/abs/2606.26815
pdf_url: https://arxiv.org/pdf/2606.26815
published: '2026-06-25'
collected: '2026-06-28'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: This paper compares different methods for forecasting the term structure
  of U.S. and European z...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-stat.ML
depth: abstract
---

### 摘要

This paper compares different methods for forecasting the term structure of U.S. and European zero-coupon government bonds using both traditional econometric and Machine Learning (ML) approaches. We compare classical models (e.g., Dynamic Nelson-Siegel (DNS) and Principal Component Analysis (PCA)) with different Neural Network (NN) architectures, including those inspired by the classical models, on the U.S. Treasury market and bonds issued by the European Central Bank (ECB). To enhance predictive performance, macroeconomic variables are incorporated. The findings for both markets are separately analyzed and compared. To this end, we propose a robust model evaluation framework combining statistical accuracy metrics - such as RMSE, MAE, and directional accuracy - with the economic relevance of a quantitative bond trading strategy. Results show that NNs consistently outperform traditional models in both forecasting accuracy and portfolio performance. For the U.S., the most effective approach is a direct-forecasting NN that incorporates DNS factors to reduce the dimensionality of zero-rate data and an Autoencoder (AE) to extract macroeconomic features, while for Europe, the optimal model is a factor-based NN using PCA-derived zero-rate factors without the integration of macroeconomic variables. Overall, the paper demonstrates how combining traditional modeling approaches with modern ML techniques and evaluation can improve yield curve forecasts and support applications in fixed-income portfolio construction.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
