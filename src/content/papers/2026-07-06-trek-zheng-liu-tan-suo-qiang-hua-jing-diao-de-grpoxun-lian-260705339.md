---
title: 'TREK: Distill to Explore, Reinforce to Refine'
title_zh: TREK：蒸馏探索+强化精调的GRPO训练增强框架
authors:
- Yuanda Xu
- Zhengze Zhou
- Kayhan Behdin
- Jelena Markovic-Voronov
- Hejian Sang
- Xiaomin Li
- Wenhui Zhu
- Xinchen Du
- Aida Rahmattalabi
- Ran He
affiliations:
- LinkedIn Corporation
- Harvard University
- Georgia Institute of Technology
arxiv_id: '2607.05339'
url: https://arxiv.org/abs/2607.05339
pdf_url: https://arxiv.org/pdf/2607.05339
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: LLM训练 · GRPO探索增强
tags:
- GRPO
- Knowledge Distillation
- Forward KL
- Agent Training
- Reasoning
one_liner: 提出分阶段蒸馏扩展GRPO采样支持的TREK框架，提升数学推理与Agent任务性能
practical_value: '- 电商导购Agent、多步商品检索Agent等场景训练遇GRPO卡在低成功率硬任务时，可直接复用TREK流程：筛选低通过率硬任务，用黑盒大模型/加推理上下文的同模型生成验证通过的轨迹，保留和当前模型似然最高的top-r样本做短时间forward-KL微调再回归GRPO，可快速提升硬场景性能，降低训练步数

  - 不需要教师模型的logits、权重等内部信号，仅需输出轨迹即可完成蒸馏，适配业务场景中只能调用GPT-4o、DeepSeek等黑盒大模型API的情况，降低对大模型权限的依赖

  - 生成式推荐、Agent任务的蒸馏可复用trimmed NLL做轨迹相似度排序，过滤距离当前学生过远的样本，避免蒸馏不稳定，比直接全量蒸馏教师轨迹效果更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GRPO作为当前主流的LLM RL训练方法，仅能优化当前策略可采样到的轨迹；在硬任务（复杂数学推理、长horizon Agent决策）场景中，学生模型的采样支持覆盖不到正确解模式，反复产出相似错误轨迹，训练陷入停滞，核心瓶颈不是奖励稀疏，而是探索覆盖不足。

### 方法关键点
- 硬prompt路由：先统计当前学生模型在每个prompt下的通过率，仅对通过率低于阈值τ_low的硬prompt调用提案源生成候选解
- 多兼容提案源：支持黑盒大模型、白盒教师、甚至添加了失败教训、多步重试、环境反馈等额外推理上下文的同模型，仅需输出验证通过的轨迹，不需要任何内部信号
- 轨迹筛选：对验证通过的提案轨迹，用截断长度归一化NLL计算与当前学生的相似度，保留top-r最接近的轨迹，避免蒸馏过远样本导致训练不稳定
- 分阶段训练：先对筛选出的轨迹做短时间forward-KL微调，将正确解模式拉入学生的采样支持，再回归常规GRPO训练做精调

### 关键实验
实验覆盖AIME 2024/2025数学推理集、ALFWorld/ScienceWorld Agent任务集，对比基线为直接GRPO训练。核心结果：Qwen3-8B上AIME 2025准确率从36.9提升至40.3，AIME 2024从47.9提升至51.1；ALFWorld成功率从75.8提升至82.8，ScienceWorld成功率从12.5翻倍至26.7，硬任务训练效率较纯GRPO提升约5倍。

### 核心结论
蒸馏的价值不只是模仿教师行为，还可主动扩展学生模型的采样支持，解决RL训练的探索不足问题。
