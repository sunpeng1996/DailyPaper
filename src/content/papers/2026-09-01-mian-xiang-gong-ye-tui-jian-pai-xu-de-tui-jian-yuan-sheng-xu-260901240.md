---
title: 'From Language to Behavior: Scaling Sequence Transformers for Industrial Recommendation
  Ranking with Rec-Native Designs'
title_zh: 面向工业推荐排序的推荐原生序列Transformer框架ReST
authors:
- Jie Chen
- Xiangqian Yu
- Yanchao Lian
- Tan Lu
- Run Yang
- Zhengchun Shang
- Xing Wang
- Cheng Chen
- Ke Hu
- Qiang Li
affiliations:
- ByteDance
arxiv_id: '2609.01240'
url: https://arxiv.org/abs/2609.01240
pdf_url: https://arxiv.org/pdf/2609.01240
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 工业推荐排序 · 序列Transformer扩展
tags:
- Sequence Transformer
- Behavior Modeling
- Ranking System
- Industrial Deployment
- Scaling Law
one_liner: 针对推荐行为序列特性设计Transformer架构，在50ms延迟内将广告平台核心营收指标提升11.93%
practical_value: '- 行为序列建模可复用Dual-Gated Attention设计：通过value gate预过滤噪声行为、output gate后调制聚合结果，在不修改attention
  softmax的前提下提升对噪声点击/浏览的鲁棒性，兼容现有高效attention内核

  - 解决序列模块被非序列特征短路的序列饥饿问题：可引入训练专用的辅助序列CVR损失、序列/非序列特征对比对齐损失，无推理开销即可强化序列模块的梯度信号，提升长序列建模收益

  - 排序系统的架构拆分可复用「重编码器+轻量交叉解码器」设计：用户侧序列编码器计算一次可复用给所有候选，解码器采用无投影KV、token专属参数化控制单候选推理开销，配合共享前缀推理可将序列模块推理成本降低20倍

  - 工业场景下扩展序列模型优先优化信号质量而非盲目加参：实验显示给编码器加MoE提5倍参数无收益，而针对时序、噪声、优化稳定性的原生设计收益更显著，符合严格延迟约束下的优化方向'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
直接套用LLM的Transformer扩展范式到推荐排序场景存在两大核心痛点：一是用户行为序列噪声大、时间间隔不规则、标注稀疏，序列模块容易被强表征的非序列特征（如用户属性）短路，出现「序列饥饿」效应，纯LLM式Transformer扩展收益边际递减；二是推荐排序存在计算不对称性，单请求下1份用户历史要匹配N个候选，LLM式单栈架构无法分别优化共享计算与候选侧计算，难以满足生产延迟要求。

### 方法关键点
- 推荐原生序列编码器：采用双门控注意力（DGA）过滤噪声行为、RoPE+多粒度RoTE融合序列顺序与物理时间信息、稳定残差归一化（SRN）解决深模型优化不稳定问题，适配行为序列特性
- 非对称编码器-解码器架构：拆分计算为可复用的重序列编码器、轻量交叉解码器，解码器采用无投影KV注意力、token专属参数化设计，控制单候选计算开销
- 训练优化：新增训练专用的辅助序列CVR损失、序列-非序列特征对比对齐损失，解决序列饥饿问题，强化序列模块梯度信号
- 系统协同设计：训练侧采用用户级共享前缀训练，复用同用户的序列编码结果，训练吞吐量提升5.8倍；推理侧采用请求级共享前缀服务，序列编码一次复用给所有候选，序列模块推理成本降低20倍

### 关键结果
在TikTok Shop Ads工业数据集、MovieLens/Amazon Books公开数据集上对比DIN、STCA、LLaMA式Transformer、HSTU等基线，同等FLOPs下ReST离线AUC最高提升0.92%；一周线上A/B测试在50ms P99延迟约束下，在线AUC提升1.31%，核心营收指标提升11.93%，已全量上线。

**最值得记住的一句话**：工业推荐场景扩展序列模型的核心瓶颈不是算力，而是针对行为序列特性的原生设计与计算复用机制，而非直接套用LLM的扩展范式
