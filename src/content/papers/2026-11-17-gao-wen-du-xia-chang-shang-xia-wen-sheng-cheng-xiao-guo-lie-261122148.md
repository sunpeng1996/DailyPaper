---
title: Long-Context Generation Is a Sampling Problem (When You Turn Up the Heat)
title_zh: 高温度下长上下文生成效果劣化本质是采样策略问题
authors:
- Allen G. Roush
- Minh Nhat Nguyen
- Ravid Shwartz-Ziv
- Judah Goldfeder
- Sanjay Basu
affiliations:
- Thoughtworks
- Apart Research
- New York University
- Columbia University
- Oracle
arxiv_id: '2611.22148'
url: https://arxiv.org/abs/2611.22148
pdf_url: https://arxiv.org/pdf/2611.22148
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: LLM解码采样 · 高温度长上下文优化
tags:
- LLM Sampling
- Long Context
- Inference Optimization
- Temperature Tuning
- Agent Generation
one_liner: 验证高温度下保持采样候选集稳定即可避免长上下文、Agent生成效果劣化
practical_value: '- 电商/广告文案生成、导购Agent多轮交互场景如需调高温度提升内容多样性，优先选用top-nσ（n≤1）、高阈值min-p采样，可避免高温度下生成乱码、逻辑崩溃，实测温度2下top-nσ较top-p的Agent任务成功率提升最高62pct

  - 工程侧可直接修改推理框架采样逻辑：先基于T=1的概率分布筛选候选集，再施加温度缩放采样，无需微调模型即可让top-H、min-p、P-less等采样器在高温度下保持T=1的生成效果，零额外训练成本

  - 内部LLM效果评测、供应商选型必须明确上报采样策略的平均候选集大小、温度值、截断顺序，避免相同模型因采样配置差异出现结果偏差：同一款Qwen3.5模型在温度2下，top-p的编码任务通过率为0，top-nσ可达62%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开源LLM普遍存在生成序列越长效果越差的问题，业界通常依赖额外长文本微调解决，成本较高；而高温度场景下采样策略对长生成、Agent任务的影响长期被低估，温度>1时常用的top-p、top-k采样会引入大量低概率噪声token，直接导致生成内容崩溃。
### 方法关键点
- 对比7种主流截断采样策略：top-p、top-k、Top-H、P-less、min-p、top-nσ、纯采样，验证温度缩放与截断顺序对候选集大小的影响
- 测试覆盖29款1B~122B参数量的开源指令微调模型，包含10项公开基准+最长1M token的needle召回任务，覆盖Agent编码、长链推理、长文生成、结构化输出、长上下文理解5类核心场景
- 核心验证逻辑：采样候选集大小随温度的增长幅度是决定高温度下生成质量的核心变量
### 关键结果
- 温度2下，Qwen3.5系列模型采用top-p、top-k采样的SWE-bench编码Agent通过率为0，采用top-nσ采样通过率可达46%~62%，所有双方分歧的任务均为top-nσ胜出
- 全基准测试下，top-nσ在高温度下的得分保持率中位数为100%（与T=1效果一致），top-p仅为26%；温度从1升到2时，top-p的候选集从平均2个暴涨至9万个，top-nσ稳定维持在1~2个
- 候选集大小与生成质量的斯皮尔曼相关系数为-0.77，候选集超过100个token时生成质量基本不可用
> 最值得记住的一句话：高温度下长上下文生成劣化不需要重新训练模型，只要保持采样候选集小且稳定即可解决
