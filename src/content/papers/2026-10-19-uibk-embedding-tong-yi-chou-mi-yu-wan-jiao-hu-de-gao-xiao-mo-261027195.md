---
title: 'UIBK-Embedding: Effective Text Retrieval by Unifying Dense and Late-Interaction
  Retrieval'
title_zh: UIBK-Embedding：统一稠密与晚交互的高效文本检索模型
authors:
- Abdelrahman Abdallah
- Mohammed Ali
- Adam Jatowt
affiliations:
- University of Innsbruck
arxiv_id: '2610.27195'
url: https://arxiv.org/abs/2610.27195
pdf_url: https://arxiv.org/pdf/2610.27195
published: '2026-10-19'
collected: '2026-10-21'
category: RAG
direction: 文本检索 · 稠密与晚交互能力融合
tags:
- Text Retrieval
- Dense Retrieval
- Late Interaction
- MaxSim
- ColBERT
- Embedding
one_liner: 单模型单索引融合稠密与晚交互检索能力，同规模下BEIR nDCG@10提升2.57个点
practical_value: '- 混合检索降本：电商商品检索、Agent RAG问答场景可直接复用现有PLAID/ColBERT索引栈，无需维护两套编码器、两个索引，省去打分融合步骤，工程复杂度降低50%以上

  - 多粒度匹配复用：「slot向量+1维tag隔离」的设计可直接迁移到商品多粒度匹配场景，把品类/价格等全局属性向量嵌入token级检索体系，无需修改检索引擎逻辑

  - 训练优化落地：蒸馏环节优先对齐融合检索得分而非单头得分，电商场景可直接用点击/转化序作为teacher信号，无需额外标注就能提升融合效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
稠密检索擅长全局语义匹配，晚交互检索（如ColBERT）擅长精准实体/短语匹配，两类方法互补性强，但当前混合检索方案需要两套编码器、两个独立索引、两次检索后再做分数融合，工程开销大、维护成本高；现有多输出编码器仍需多套索引和独立打分逻辑，无法实现端到端单栈融合。
### 方法关键点
- 架构：共享18层ModernBERT-base主干，晚交互头和稠密头各独立4层顶层，仅新增20.1M参数，总参数量179M
- 表示融合：将稠密全局向量拆分为3个slot向量追加到token向量列表，通过向量第1维的正负tag隔离slot与token，原生MaxSim会自动拆分计算词级别匹配分+加权稠密余弦分，无需修改现有索引和打分逻辑
- 训练：除单头NCE对比损失外，新增cross-encoder的融合得分蒸馏损失和锚定损失，保证单头能力不下降的同时提升融合效果
### 关键结果
BEIR数据集nDCG@10达59.79，比同规模最优晚交互模型LateOn高2.57点，等长文档下仍高2.10点，15个数据集全部领先；仅1.5B参数以上模型效果超过它。去污染BEIR上nDCG@10达61.55，领先LateOn 1.19点，8/12数据集占优。编码速度仅比LateOn慢9%，索引大小相当，比双模型混合检索快1.7倍，索引小22%。
最值得记住的一句话：零侵入改造现有晚交互检索栈就能实现混合检索的效果与成本双优。
