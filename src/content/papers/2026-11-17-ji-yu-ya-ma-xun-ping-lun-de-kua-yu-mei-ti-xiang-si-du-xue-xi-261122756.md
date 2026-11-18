---
title: Learning Cross-Domain Media Similarity from Amazon Reviews
title_zh: 基于亚马逊评论的跨域媒体相似度学习方法
authors:
- Gabrielly Xavier dos Santos
- Lucas Dias Cler
- Luciana Fujii Pontello
- Olga Goussevskaia
affiliations:
- Universidade Federal de Minas Gerais (UFMG)
arxiv_id: '2611.22756'
url: https://arxiv.org/abs/2611.22756
pdf_url: https://arxiv.org/pdf/2611.22756
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 跨域推荐 · 评论特征挖掘
tags:
- Cross-Domain Recommendation
- Review-based Recommendation
- Item Similarity
- Collaborative Filtering
- Feature Engineering
one_liner: 基于公开评论特征监督学习跨域物品相似度，无需依赖平台私有交互数据
practical_value: '- 跨域冷启场景下，当目标域交互数据缺失时，可优先引入热度类特征（如评论量差）替代纯语义特征，提升跨域相似度预估准确率

  - 跨域相似度模型训练无需大量目标域标注，仅在训练集中混入10%以内的跨域样本即可大幅缓解零样本迁移失效问题

  - 处理百万级评论数据做特征工程时，可采用DuckDB+Parquet的方案实现外存批处理，规避内存瓶颈同时提升处理效率

  - 特征迭代可参考SHAP归因结论：同域推荐优先优化语义特征，跨域推荐优先优化热度、流行度类行为特征'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统CF类推荐高度依赖平台私有用户交互数据，独立开发者、中小平台及研究者难以获取，跨域场景下用户重叠度低的问题进一步放大，现有方法要么需要部分交互数据支持，要么依赖预构建的商品关联图，泛用性差，亟需基于公开可获取的评论数据构建跨域物品相似度模型，替代私有交互信号。

### 方法关键点
- 监督信号构建：以用户评论历史中的物品共现频率为 ground truth，同域对要求共现≥5次，跨域对要求共现≥2次，用余弦相似度计算物品对标签
- 特征工程分4类：语义特征（单品评论聚合后提取TF-IDF Top50关键词，输入SBERT生成嵌入）、时序特征（单品活跃年份的Jaccard相似度）、热度特征（单品评论量、两两评论量差）、评分特征（单品平均评分、两两评分差），拼接为775维混合向量
- 训练策略：采用XGBoost作为回归模型，训练前对数据做随机欠采样避免长尾偏差，分同域训练、混合训练、跨域训练三种模式验证效果

### 关键实验
基于2023亚马逊评论数据集的图书、电影两个域，共5M+物品、46M+评论、16M+用户；零样本同域转跨域R²为-4.00（完全失效），训练集混入少量跨域样本后跨域测试R²提升至0.32，定向迁移中电影→图书R²达0.76、图书→电影R²达0.38；特征 ablation 显示移除热度特征后跨域R²降至-0.99，移除语义特征降至-1.78。

### 核心结论
同域相似度预估高度依赖语义特征，跨域场景下热度类行为特征才是泛化的核心锚点，少量跨域训练样本即可大幅缓解迁移失效问题。
