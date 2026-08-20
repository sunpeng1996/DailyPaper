---
title: Multimedia Asset Personalization via Multimodal Embeddings at Netflix
title_zh: Netflix基于多模态嵌入的多媒体宣传资产个性化系统
authors:
- Emma Yanyang Kong
- Aditya Deshpande
- Bowei Yan
- Asad Abbasi
- Santiago Castro
- Avneesh Saluja
- David Fagnan
- Ashish Rastogi
affiliations:
- Netflix
- Cohere
arxiv_id: '2608.18322'
url: https://arxiv.org/abs/2608.18322
pdf_url: https://arxiv.org/pdf/2608.18322
published: '2026-08-18'
collected: '2026-08-20'
category: RecSys
direction: 多模态推荐 · 工业落地与冷启动优化
tags:
- multimodal_embedding
- cold_start
- two_tower
- CLIP
- proxy_task
- industrial_recsys
one_liner: 在Netflix生产环境落地多模态嵌入的封面/视频预览个性化，解决冷启动并提效实验流程
practical_value: '- 工程上可复用三层预计算架构：资产嵌入、item tower输出、用户-资产匹配结果全部预计算，把多模态计算延迟完全从请求路径剥离，无需放宽在线SLA，适合电商商品封面、短视频预览等多模态推荐场景落地

  - 可复用小流量探索+IPS加权离线评估方案：用固定占比的随机探索流量记录真实曝光propensity，无需倾向性估计即可得到无偏离线评估结果，大幅降低A/B测试试错成本

  - 多模态嵌入选型可复用线性探针proxy任务：通过预测非个性化资产热度赢家提前筛除不合格embedding候选，无需跑全链路训练和A/B测试即可缩小选型范围，节省算力和时间

  - 跨场景模型合并trick：多场景（不同端/展示位）推荐目标同源时可合并为统一模型，训练时按交互长期价值而非曝光量加权，既减少运维成本，还能通过跨场景信号转移提升冷启动效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

#### 动机
传统宣传资产（封面图、视频预览）个性化模型完全依赖ID交互历史，内容无感，新资产、新场景冷启动问题突出，且多场景分拆模型运维成本高，需要一套可落地的多模态嵌入融合方案解决上述问题。
#### 方法关键点
- 架构层搭建统一Embedding Store，多模态基座生成的资产嵌入预计算存储，训练与在线推理复用，解耦基座模型迭代与下游推荐系统部署
- 封面个性化：将CLIP图像嵌入拼接至双塔模型item塔，合并5个分画布独立模型为统一架构，训练时按交互的长期价值加权平衡不同画布样本权重；搜索场景直接复用CLIP图文对齐能力，新增余弦相似度项实现query感知封面排序，几乎无额外成本
- 视频预览个性化：自研三模态基座MediaFM，融合视觉、音频、字幕特征，用掩码镜头建模自监督预训练，嵌入接入双塔item塔
- 实验提效：设计线性探针proxy任务，预测单内容的非个性化最优资产，提前筛选embedding候选，降低全链路实验成本
#### 关键结果
- 封面统一模型+CLIP方案在线核心发现指标提升0.127%，UI改版冷启动场景下核心指标提升0.233%，流媒体时长提升0.184%
- 搜索query感知封面无额外建模成本，播放率提升0.36%
- 视频预览场景MediaFM相对ID基线离线IPS提升0.38%，在线流媒体时长提升0.193%
- proxy任务准确率与离线、在线指标完全对齐，已作为MediaFM新版本上线门槛
#### 核心经验
内容信号与模型容量互补，单独新增内容特征或单独合并模型均无显著收益，二者结合才能最大化冷启动与全场景效果
