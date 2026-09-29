---
title: Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs
title_zh: 合并MoE大模型中仅路由漂移不足以作为路由故障的诊断依据
authors:
- Yuanyi Wang
- Yanggan Gu
- Su Lu
- Guanghao Zhu
- Pengkai Wang
- Yifan Yang
- Congkai Xie
- Zhaoyi Yan
- Jianmin Wu
- Hongxia Yang
affiliations:
- The Hong Kong Polytechnic University
- InfiX.ai
arxiv_id: '2609.32821'
url: https://arxiv.org/abs/2609.32821
pdf_url: https://arxiv.org/pdf/2609.32821
published: '2026-09-26'
collected: '2026-09-29'
category: LLM
direction: MoE大模型合并 · 路由故障诊断
tags:
- MoE
- Model Merging
- Routing Drift
- Router Repair
- LLM
one_liner: 明确合并MoE的路由漂移不等于故障，提出任务导向诊断标准与路由分析修复工具
practical_value: '- 业务侧合并MoE模型（如多场景推荐召回MoE、生成式文案MoE）后排查性能下降时，不要直接将路由漂移等同于故障，优先通过固定非路由参数的干预测试验证路由对业务指标的实际影响，避免无效修复

  - 做MoE路由优化时，无需盲目对齐源模型的路由结果，不同专家选择可能输出余弦相似度0.896-0.976的相似混合结果，优先验证路由修改的实际业务收益，而非只看重路由匹配度

  - 可复用论文开源的反事实路由分析工具，快速定位路由漂移的根因是输入表征漂移还是路由参数变化，降低问题排查成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE 模型合并无需联合重训即可融合多个专用模型能力，是大模型低成本能力扩展的主流方案，但合并后普遍出现的路由漂移（token分配的专家与源模型不一致）长期被默认等同于路由故障，直接触发无差别路由对齐修复，既浪费算力，也常出现修复后无收益甚至性能下降的问题，核心原因是缺乏对路由漂移实际影响的因果验证标准。

### 方法关键点
- 交叉干预归因：通过替换源/合并模型的路由输入、路由参数，精准拆解路由漂移的来源是输入表征漂移还是路由参数变化
- 任务导向故障定义：将路由故障明确为「固定非路由参数时，更换路由策略可恢复的任务损失」，替代过往基于与源模型路由一致性的判定规则
- 选择性路由修复（SRR）：基于源模型token似然优势，仅修正合并模型路由的部分参数，最小化修复对模型的影响

### 关键结果
实验覆盖DeepSeekMoE、OLMoE、Qwen3-MoE三个主流MoE架构，4种主流合并方法，8个通用基准测试：
1. 77.7%-96.9%的路由漂移由输入表征漂移导致，仅最多1.8%由路由参数变化引发
2. 路由漂移的JS散度预测源路由恢复收益的AUROC仅0.47-0.52，接近随机猜测
3. 源路由恢复、SRR修复均未带来统计显著的任务精度提升，相对未修复基线的精度变化在-0.056pp到+0.139pp区间波动

### 核心结论
路由漂移本身不是路由故障的证据，路由修复的合理性必须通过任务级的干预效果验证，而非与源模型的路由一致性。
