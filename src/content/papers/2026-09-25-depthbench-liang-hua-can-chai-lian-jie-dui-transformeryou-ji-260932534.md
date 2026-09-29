---
title: 'DepthBench: Measuring How Residual Connections Enable More Computational Depth'
title_zh: 《DepthBench：量化残差连接对Transformer有效计算深度的增益》
authors:
- Keyu Wang
- Yangyi Huang
- Jiale Kang
- David González-Martínez
- Weiyang Liu
- Shiwei Liu
affiliations:
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- Tübingen AI Center
- The Chinese University of Hong Kong
arxiv_id: '2609.32534'
url: https://arxiv.org/abs/2609.32534
pdf_url: https://arxiv.org/pdf/2609.32534
published: '2026-09-25'
collected: '2026-09-29'
category: LLM
direction: LLM架构优化 · 残差连接设计
tags:
- Transformer
- Residual Connection
- Model Scaling
- DepthBench
- LLM Optimization
one_liner: 提出固定参数预算的DepthBench基准，验证残差结构决定Transformer深度缩放的有效性
practical_value: '- 端侧部署的推荐/Agent小LLM可采用HC/Full AttnRes残差结构，同参数下采用深窄形态提升效果，适配端侧内存限制

  - 业务场景的文案生成、query理解小LLM可将Pre-LN替换为Full AttnRes，调整宽深比无需加参即可提升效果

  - 深窄模型KV cache占用是宽浅模型的2倍以上，推理时延更高，上线前需做kernel优化平衡效果与latency'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer深度缩放面临深度诅咒：仅增加架构深度无法带来匹配的效果增益，甚至性能下降。不同残差、归一化优化方案的收益缺乏统一可控的对比，无法明确哪些架构能真正将架构深度转化为有效计算深度，支撑模型缩放决策。
### 方法关键点
- 固定总参数量与训练配方，调整宽深比`dmodel/nlayer`覆盖7种从宽浅到深窄的模型形态，排除参数量、训练超参差异的干扰
- 覆盖10种代表性Transformer架构：含Pre-LN基线、归一化变种（Sandwich-LN、LNS等）、多流残差（HC、mHC）、跨层访问（Full AttnRes、Block AttnRes等）
- 评估维度包含预训练验证loss、下游领域（代码、STEM、数学）NLL，以及层级表征多样性、因果依赖、层交换敏感度等深度利用率指标
### 关键结果
在FineWeb-Edu数据集预训练200M~1.6B参数模型：
- Pre-LN及归一化变种随模型变深窄，400M参数下验证loss最高上升0.023，深窄架构反而掉点
- HC和Full AttnRes随模型变深窄，400M参数下验证loss最高下降0.03，70层极端深窄形态下仍持续提升，下游STEM、数学任务NLL最高下降3%
- 深窄模型KV cache占用是宽浅模型的2倍以上，GPU推理耗时提升约2倍，存在明确的效果-效率tradeoff
### 核心结论
残差连接设计是Transformer深度能否作为有效缩放轴的核心决定因素，仅优化归一化方案无法释放深度的潜力
