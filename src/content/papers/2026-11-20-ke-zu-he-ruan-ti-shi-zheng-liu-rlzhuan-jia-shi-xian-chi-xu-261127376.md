---
title: 'Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training'
title_zh: 可组合软提示蒸馏RL专家：实现持续后训练的新方法
authors:
- Zhen Zhang
- Changyi Yang
- Xuehai He
- Chengzhi Liu
- Yutong Yin
- Ziyue Liu
- Zhuoran Yin
- Yangmin Li
- Zhihan Liu
- Jisen Li
affiliations:
- University of California, Santa Barbara
- Carnegie Mellon University
- NVIDIA
- Apple
- Northwestern University
arxiv_id: '2611.27376'
url: https://arxiv.org/abs/2611.27376
pdf_url: https://arxiv.org/pdf/2611.27376
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 持续后训练 · 软提示蒸馏
tags:
- Soft Prompt
- Knowledge Distillation
- Reinforcement Learning
- Continual Learning
- Inference Efficiency
one_liner: 将RL专家蒸馏为独立软提示，冻结骨干直接拼接组合，匹敌MOPD性能且推理开销接近原生
practical_value: '- 电商多垂类（家电/美妆/3C等）的RL优化专家可分别蒸馏为独立软提示，无需修改骨干LLM即可灵活组合适配跨域推荐、导购Agent等场景，避免灾难性遗忘

  - 推理侧复用相同冻结骨干，不同请求的软提示可混batch部署，吞吐量比rank-4 LoRA高2.4倍，P95首Token延迟降低2.27倍，适合多用户个性化垂类需求的大规模服务

  - 新增垂类/热点能力仅需训练对应软提示，无需重训原有模型或其他提示，适合大促、热点事件等临时需求的快速上线'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RL后训练通常产出单领域专家，传统整合方案（权重合并、多教师在线蒸馏MOPD）每次新增专家都需要重训全模型，易侵蚀非目标域原有能力，且推理部署开销高，无法适配专家持续新增的业务场景。
### 方法关键点
- 冻结预RL骨干模型，将每个RL专家独立蒸馏为256维软提示，训练时50%样本加入随机上下文前缀提升组合鲁棒性，无需联合训练即可直接拼接多个软提示实现能力组合
- 蒸馏仅使用对应专家的验证器过滤后的回复数据，优化长度归一化的负对数似然损失，全程仅更新软提示参数
- 推理时直接将选中的软提示拼接在系统消息位，支持动态增删专家，完全不修改骨干权重
### 关键实验
覆盖23个数学、代码、Agent任务，对比MOPD、权重合并、LoRA合并等基线：单软提示在22/23任务上恢复至少90%的RL专家增益，15个任务性能超过原专家；4个跨域软提示拼接后域内平均得分67.83，与MOPD的67.79基本持平，6个域外基准平均得分56.6，远超MOPD的53.5；单B200上32并发请求时，软提示吞吐量仅比原生骨干低1.5%，是rank-4 LoRA的2.4倍，P95首Token延迟降低2.27倍。
### 核心结论
将专家能力编码到输入空间的软提示而非模型权重，是实现低成本、无遗忘持续后训练的可行路径
