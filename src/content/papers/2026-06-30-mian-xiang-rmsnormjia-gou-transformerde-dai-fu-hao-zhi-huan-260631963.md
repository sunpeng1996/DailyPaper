---
title: Signed-Permutation Coordinate Transport for RMSNorm Transformers
title_zh: 面向RMSNorm架构Transformer的带符号置换坐标迁移方法
authors:
- John Sweeney
affiliations:
- Sideplane AI
arxiv_id: '2606.31963'
url: https://arxiv.org/abs/2606.31963
pdf_url: https://arxiv.org/pdf/2606.31963
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: LLM训练 · 模型权重坐标对齐
tags:
- RMSNorm
- Model Merging
- LoRA
- SAE
- Weight Alignment
one_liner: 针对RMSNorm Transformer提出带符号置换对齐方法，解决跨checkpoint坐标迁移失效问题
practical_value: '- 迁移RMSNorm架构LLM（Llama、Qwen等）的LoRA、steering vector、SAE等坐标绑定工具时，必须采用Bd带符号对齐而非仅置换对齐，可避免性能灾难性下降，比如LoRA准确率跌到随机水平、SAE重建完全失效

  - 跨训练checkpoint做坐标迁移时，不要直接匹配两端点，沿训练路径组合每步的局部Bd对齐结果，可将坐标恢复率从60%提升至90%以上，大幅提升工具跨微调轨迹的复用率

  - 做RMSNorm模型合并、优化器热启动迁移时，严格遵循论文给出的Bd变换规则，可消除合并后的性能barrier，保证AdamW状态迁移后训练轨迹不偏离

  - 若基于LLM做神经元级可解释性、用户意图归因类工作，必须显式指定Bd规范，否则跨模型/跨训练轨迹的坐标级结论完全不可复现'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM工作流中需要频繁跨checkpoint迁移坐标绑定的各类artifact，包括steering vector、SAE、LoRA权重、神经元归因集合、优化器状态等，但此前主流的仅置换对齐方法仅适配LayerNorm架构，而Llama、Qwen等绝大多数开源LLM采用的RMSNorm架构，其残差流存在独立坐标符号翻转的对称性，仅置换对齐完全忽略这一维度，会导致迁移的artifact彻底失效，严重影响跨训练轨迹的工具复用、模型合并等工作流的可靠性。

### 方法关键点
- 理论证明RMSNorm Transformer的原生离散规范是带符号置换群Bd，而非LayerNorm对应的置换群Sd，忽略符号的对齐会导致权重更新的期望平方误差达到更新本身能量的2倍
- 提出符号边缘化匈牙利匹配算法，基于激活的绝对相关性做排列匹配，再恢复对应坐标的符号，从根源上解决带符号对齐的结构天花板问题
- 提出沿训练轨迹组合每步局部Bd对齐结果的坐标迁移方案，替代传统的两端点直接匹配
- 给出steering vector、LoRA、SAE、AdamW状态等所有常见坐标绑定artifact的标准化Bd变换规则

### 关键结果
在Qwen2.5、Llama2、TinyLlama等主流RMSNorm模型上测试，对比仅置换Sd对齐基线：1500步跨训练轨迹坐标恢复率从60.3%提升至91.1%；情感steering vector效果保留率从17.2%提升至95.8%；TinyLlama SAE重建NMSE从1.08降至0.004；SST-2任务LoRA增益保留率从-0.5%提升至99.7%；Bd对齐的AdamW状态迁移可完全保留训练轨迹，而Sd对齐的状态会导致轨迹完全偏离。

### 核心结论
所有基于RMSNorm架构LLM的坐标绑定类工具复用、模型合并工作，都必须采用带符号置换对齐，仅置换对齐的结果基本不可用
