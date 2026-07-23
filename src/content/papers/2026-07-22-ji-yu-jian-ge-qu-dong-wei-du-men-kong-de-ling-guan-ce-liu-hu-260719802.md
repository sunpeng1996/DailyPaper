---
title: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating
title_zh: 基于间隔驱动维度门控的零观测流失用户召回方法
authors:
- Jiandong Ding
- Tianying Liu
- Fuyuan Liu
- Huijie Qin
- Tiandeng Wu
affiliations:
- Fudan University
- Huawei Technologies
arxiv_id: '2607.19802'
url: https://arxiv.org/abs/2607.19802
pdf_url: https://arxiv.org/pdf/2607.19802
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 序列推荐·流失用户召回
tags:
- Sequential Recommendation
- User Reactivation
- Cold Start
- Dimensional Gating
- PEFT
one_liner: 为冻结的序列推荐骨干添加轻量维度门控插件，大幅提升久未活跃用户召回效果
practical_value: '- 流失用户分层运营：可按用户沉默间隔Δt拆分<30d/30-90d/90-180d/180-365d/>365d人群，单独优化久未活跃用户的推荐效果，避免统一模型在长尾人群效果坍塌

  - 低侵入式模型改造：若现有序列推荐骨干（SASRec/BERT4Rec等）已上线且与其他服务共享embedding，可直接复用冻结骨干加DeltaGate插件，仅训练66K参数（2-4%额外开销）无骨干漂移，上线成本极低

  - 效果权衡方案：允许全量重训时可将log(1+Δt)特征拼接进输入端到端训练，效果优于插件方案，但需评估embedding漂移对其他依赖模块的影响；稳定性优先场景选插件方案

  - 可解释性监控：可将维度门的均值作为历史兴趣置信度指标，监控不同沉默间隔用户的历史兴趣保留比例，辅助排查召回结果的个性化程度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型默认用户历史行为时效性一致，但流失用户长时间无交互后，历史兴趣可靠性大幅下降，传统新用户冷启动方案不适配这类有历史行为但久未活跃的零观测召回场景；主流时间感知序列推荐仅建模交互间隔，对用户最后一次交互后的长间隔适配效果差，亚马逊Video Games数据集里>365天的流失用户占比达19.2%，是不可忽视的高价值运营人群。

### 方法关键点
- 提出DeltaGate轻量插件，完全冻结原有序列推荐骨干，仅在输出层新增维度级门控，参数开销仅2-4%
- 门控输入同时拼接log(1+Δt)（压缩长间隔取值范围）和用户预间隔历史表征，通过2层MLP输出0-1的维度权重
- 最终用户表征为维度加权的历史表征与零初始化全局先验的融合，既保留稳定长期兴趣，也适配兴趣漂移
- 提出Gap-Synthesize评估协议，按自然沉默间隔拆分用户桶，避免时间切分带来的评估偏差

### 关键结果
在3个亚马逊电商数据集（Video Games/CDs & Vinyl/Movies & TV）上对比SASRec、GRU4Rec、BERT4Rec、TiSASRec等基线：
- >365天间隔的Video Games数据集上，DG-SASRec Hit@10达0.047，较原生SASRec的0.031提升51.6%；DG-BERT4Rec Hit@10达0.046，较原生BERT4Rec的0.025提升84%
- 端到端重训方案较插件方案效果更高（>365天Hit@10达0.08），但参数量是插件的40倍，embedding漂移达139.7%

最值得记住的结论：针对流失用户召回，低侵入的冻结骨干插件方案可以用极低成本获得可观的效果提升，在稳定性要求高的工业场景性价比远高于全量重训。
