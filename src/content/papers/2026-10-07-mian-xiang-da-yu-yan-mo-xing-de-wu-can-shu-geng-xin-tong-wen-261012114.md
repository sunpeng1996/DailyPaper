---
title: Universal Textual Teaching for LLMs
title_zh: 面向大语言模型的无参数更新通用文本教学框架
authors:
- Zhanyi Lu
- Huan Wang
affiliations:
- Westlake University
arxiv_id: '2610.12114'
url: https://arxiv.org/abs/2610.12114
pdf_url: https://arxiv.org/pdf/2610.12114
published: '2026-10-07'
collected: '2026-10-12'
category: LLM
direction: 大模型无参数知识蒸馏
tags:
- Knowledge Distillation
- Prompt Optimization
- LLM Alignment
- Parameter Free
- Textual Primer
one_liner: 通过多角色大模型交互生成可跨模型复用的文本Primer，实现无参数更新的知识蒸馏
practical_value: '- 可复用UTT多角色交互框架，将业务场景（如推荐理由生成、Query改写）中优质大模型经验蒸馏为自然语言Primer，无需微调小模型，适配API调用的商用模型场景，大幅降低训练成本

  - 借鉴知识-gap筛选逻辑，先统计业务场景下大小模型的效果差样本，针对性生成教学内容，比通用prompt优化效率更高，可快速提升小模型在细分任务上的表现

  - 利用Primer的跨模型可迁移性，适配业务多模型部署场景，同一任务的Primer可直接给多个不同调用模型使用，无需为每个模型单独做微调或prompt优化

  - 可用于Agent技能沉淀：将复杂任务（如大促选品策略、用户投诉处理）的优质经验沉淀为通用Primer，新Agent实例直接加载即可复用，无需重新训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型知识蒸馏方法均需更新学生模型参数，知识与特定模型架构深度绑定，不可解释、无法跨模型复用，也不适用于仅支持API调用的不可训练商用模型，亟需无参数更新、可解释、可跨模型迁移的知识蒸馏方案。
### 方法关键点
- 知识-gap构建：配对评估Teacher与Student模型在目标任务上的表现，筛选Teacher效果优于Student的样本作为蒸馏训练集，同时划分留存集（Student表现优于Teacher）、前沿集（两者均无法解决）用于效果验证
- 多角色闭环Primer合成：Student尝试解题，Prompter基于错误反馈生成教学指令，Teacher输出针对性示范，Synthesizer整合有效经验更新Primer，每轮验证新Primer效果不下降才更新，全程冻结所有模型参数
- Primer为自然语言形式的知识手册，包含任务规则、推理策略、常见避坑点，推理时直接拼接到输入上下文即可生效
### 关键实验
在KernelBench（GPU代码生成）、Omni-MATH-2（奥数级数学推理）两个高难度任务上测试，对比prompt优化（APE、MIPROv2、GEPA）、参数式蒸馏（SeqKD、Fine-tune-CoT等）两类基线：
- 效果提升显著：KernelBench准确率从9.4%提升至48.6%，数学推理准确率从27.6%提升至51.7%，比最优参数式KD基线高出7.2个百分点
- 跨模型迁移性强：Primer无需重新合成，直接给未参与训练的其他Student模型使用，最高可提升31.5个百分点准确率
### 核心结论
自然语言可以作为跨模型通用的可部署知识载体，为大模型知识迁移提供了无参数更新的全新路径
