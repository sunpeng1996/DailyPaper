---
title: 'From Extraction to Navigation: Progressive Retrieval with Indirectly Infinite
  Depth'
title_zh: 从抽取到导航：间接无限深度渐进式检索框架IID-Nav
authors:
- Linxiao Che
- Shanshan Huang
- Haitao Lu
- Yijia Sun
- Qiang Luo
- Ruiming Tang
- Han Li
- Kun Gai
- Guorui Zhou
affiliations:
- Kuaishou Technology
- Unaffiliated
arxiv_id: '2606.29970'
url: https://arxiv.org/abs/2606.29970
pdf_url: https://arxiv.org/pdf/2606.29970
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: 大规模推荐检索 · 状态化图导航
tags:
- Personalized Retrieval
- Graph Navigation
- Large-Scale RecSys
- Search Drift
- Stateful Learning
one_liner: 提出状态化渐进检索框架IID-Nav，通过跨请求状态持久化实现无限深度探索，解决兴趣隧道与搜索漂移问题
practical_value: '- 可借鉴跨请求状态持久化思路，打破单请求latency对检索深度的限制，不需要增加单次请求计算量，就能实现渐进式深层兴趣探索，适合电商/短视频推荐召回场景

  - 可复用协同图（Swing构建）+ 语义图（LLM多模态embedding构建）的异质图结构，同时利用行为信号和内容信号，兼顾 exploitation 和长尾/冷启
  exploration

  - 针对多跳图检索的图硬负采样策略可直接复用：采样拓扑相近但意图无关的负样本训练，能有效抑制多跳搜索的误差累积和漂移问题

  - 单次请求固定2跳的设计平衡效果与效率，工业落地难度低，910的QPS符合生产环境100ms以内的延迟要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统大规模推荐检索受限于单请求的物理延迟约束：静态i2i/两塔匹配会产生兴趣隧道效应，只能在用户历史行为的局部聚类内召回，无法探索深层长尾兴趣；现有结构化索引方法依赖静态入口和固定拓扑，多跳搜索过程容易偏离用户真实意图，出现搜索漂移，检索深度受限于单请求预算，无法穿透稀疏的兴趣区域，因此需要新范式打破深度和延迟的矛盾。

### 方法关键点
- 提出Indirectly Infinite Depth（IID）机制：通过跨请求缓存上一轮检索的前沿状态，将探索深度累积到时间维度，单次请求仅做固定2跳探索，既实现逻辑上的任意深度遍历，又不增加单请求延迟
- 构建异质导航环境：用Swing算法构建基于用户协同行为的协同图，用多模态LLM提取item元特征构建语义图，融合两类路径实现互补
- 目标感知判别器：采用目标注意力机制建模用户和候选的交叉交互，替代传统两塔结构，实现意图驱动的主动路由
- 轨迹感知学习：设计图硬负采样，从导航图中采样拓扑相近但意图无关的硬负样本，结合InfoNCE和margin pairwise损失训练，抑制搜索漂移

### 关键实验结果
在淘宝UserBehavior、MovieLens、十亿级快手工业数据集上测试，对比DSSM、Kuaiformer、TDM、NANN等SOTA基线，工业数据集上IID-Nav的Recall@500达到0.2408，相对最优基线提升36.35%，NDCG@500提升36.98%，QPS达910满足生产要求；在线A/B测试显示总使用时长提升0.3%-0.4%，核心交互指标提升最高0.566%； ablation验证去掉图硬负采样后Recall@500下降8.26%，验证了其抑制漂移的作用。

最值得记住的结论：将检索深度从单请求的物理约束中解耦，通过跨请求状态累积实现任意深度探索，同时保持单请求低延迟
