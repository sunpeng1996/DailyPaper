---
title: Mutable Low-Rank Sketches for Retrain-Free Recommendation
title_zh: 用于免重训推荐的可变低秩速写结构
authors:
- Hector J. Garcia
- Nick Clayton
affiliations:
- University of Michigan
- Criteo
arxiv_id: '2607.15242'
url: https://arxiv.org/abs/2607.15242
pdf_url: https://arxiv.org/pdf/2607.15242
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统 · 免重训实时用户embedding更新
tags:
- Low-Rank Factorization
- Real-Time Recommendation
- Cold-Start
- KP-Tree
- Collaborative Filtering
one_liner: 基于KP-tree与固定低秩投影，实现免重训的实时用户embedding更新与亚毫秒级冷启动
practical_value: '- 新用户冷启动场景可直接复用该架构：固定低秩item投影矩阵无需实时更新，新用户仅需将少量交互存入KP-tree，投影即得可用embedding，P50延迟低至0.49ms，适合电商新客首屏推荐场景

  - 稀疏交互场景（绝大多数电商/内容推荐密度远低于5%）优先选择norm-proportional采样构建低秩速写，相比均匀采样可提升40~130%的item覆盖，显著降低预测误差

  - 可构建混合更新架构：头部高活用户沿用现有增量训练/动态embedding方案保证精度，长尾低活用户用该可变速写方案，大幅降低长尾用户更新算力开销

  - 漂移触发重训逻辑可复用：通过norm divergence、投影残差两个低成本信号判断是否需要重训低秩矩阵，替代无差别周期性全量重训，节省3~5倍算力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
两阶段推荐的普遍瓶颈是embedding陈旧：用户新产生的交互要等到下一轮模型重训才能生效，传统增量方法如eALS、FunkSVD需要更新因子参数，耦合了数据新鲜度与模型重计算成本，无法做到亚毫秒级的实时更新，冷启动场景下新用户要等全量训练才能拿到个性化结果，效率极低。

### 方法关键点
- 解耦数据新鲜度与模型更新：一次性拟合固定低秩投影矩阵Vk作为item embedding，后续无需修改模型参数
- 用KP-tree（带求和聚合的稀疏线段树）存储每个用户的偏好向量，支持O(logn)的更新、查询、按模加权采样
- 用户新交互产生后仅需更新自身KP-tree，embedding实时通过固定Vk投影计算得到，无需梯度计算
- 理论保证每新增一条观测，投影误差边界单调收窄，不会出现SGD类方法更新后精度下降的问题
- 通过norm divergence和投影残差两个低成本信号判断是否需要重构Vk，避免无意义的周期性重训

### 关键实验
在KuaiRec数据集上，仅读取1.8%的数据就达到0.810 RMSE，优于读取100%数据的ALS（0.822 RMSE），单batch更新速度比eALS快8倍；新用户首条交互后<1ms即可生成个性化推荐，RMSE仅比全量ALS高0.05；在密度<5%的稀疏场景下，KP-tree的norm-proportional采样比均匀采样提升40~130%的item覆盖，RMSE最多降低0.32；单核心端到端推荐延迟P95仅2.5ms，吞吐量达927 QPS。

### 核心结论
可变低秩速写在latency-accuracy tradeoff上开辟了新的落点，亚毫秒级冷启动和单调更新安全性，在长尾低活用户、新客实时推荐等场景下收益远高于精度损失。
