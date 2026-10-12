---
title: Multi-Stream Attention Residuals
title_zh: 多流注意力残差（MSAR）：低开销提升大模型预训练效率的残差架构
authors:
- Xiaohan Qin
- Xiangdong Zhang
- Tuo Dai
- Sunan Zou
- Huaijin Wu
- Yebin Yang
- Zhuo Xia
- Lin Yao
- Yuliang Liu
- Junchi Yan
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Xiaohongshu Inc.
- Peking University
- Independent Researcher
arxiv_id: '2610.13630'
url: https://arxiv.org/abs/2610.13630
pdf_url: https://arxiv.org/pdf/2610.13630
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 大模型预训练 · 残差架构优化
tags:
- MSAR
- Residual Connection
- MoE LLM
- Pre-training Efficiency
- Transformer Architecture
one_liner: 将单流深度注意力残差扩展为多流结构，极低开销下大幅提升MoE大模型预训练效率与下游性能
practical_value: '- 业务侧垂域小模型/LLM微调时，可直接替换原残差连接为MSAR，仅增加<0.5% FLOPs即可获得显著效果提升，无需调整其他训练配置

  - 长序列用户行为建模的推荐/搜索场景，可复用MSAR的多尺度因果卷积设计，无需额外存储开销即可增强多尺度上下文依赖感知能力

  - 训练电商垂域MoE模型（文案生成/商品理解/多模态检索）时，MSAR的1.58×等损失训练加速可直接降低训练成本，相同算力下可覆盖更多垂域数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Transformer深度缩放时，标准残差连接的单流累加模式会导致早期层特征被逐步稀释，深层无法有效检索早期信息，导致深度增加的收益低于预期；现有改进方案AttnRes为单流深度注意力，mHC的多流设计头部多样性不足，均无法充分释放多头深度注意力的性能潜力。
### 方法关键点
- 上下文流扩展：通过多尺度（核大小{4,8,12}）因果深度卷积，将单流残差源扩展为4个全维度流，对应不同局部上下文感受野，不破坏隐藏表示的完整性
- 分流通路设计：每个流独立训练伪查询，单独执行深度注意力检索，再通过轻量级自适应标量混合器将多流检索结果融合为目标层输入
- 高效工程实现：仅存储单流块摘要，按需计算多流表示，存储、通信成本与AttnRes持平，28B MoE场景下仅增加0.3%激活参数、0.5%训练FLOPs
### 关键结果
在18B、28B两个MoE模型规模上，对比Vanilla残差、mHC、AttnRes三个基线，覆盖12个通用、代码数学、中文理解下游基准：
- 18B场景平均下游得分45.7，较AttnRes提升3.9，较Vanilla提升8.2；28B场景平均得分52.4，较AttnRes提升3.0
- 等损失下训练计算加速1.58×，高于AttnRes的1.35×、mHC的1.30×
> 最值得记住的一句话：以不到1%的额外训练开销，就能通过残差架构优化获得近60%的大模型预训练效率提升，是现有大模型训练的低成本升级方案
