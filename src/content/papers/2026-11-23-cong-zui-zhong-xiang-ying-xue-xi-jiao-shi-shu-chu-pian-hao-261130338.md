---
title: Learning Teacher Output Preferences from Final Responses for Reasoning Distillation
title_zh: 从最终响应学习教师输出偏好的推理蒸馏方法
authors:
- Hongli Shen
- Shaopeng Fu
- Qinbo Zhang
- Jian Li
- Di Wang
affiliations:
- King Abdullah University of Science and Technology
- Stony Brook University
arxiv_id: '2611.30338'
url: https://arxiv.org/abs/2611.30338
pdf_url: https://arxiv.org/pdf/2611.30338
published: '2026-11-23'
collected: '2026-11-24'
category: Training
direction: 推理蒸馏 · CoT跨模型重构
tags:
- CoT
- Knowledge Distillation
- DPO
- Reasoning
- LLM
one_liner: 提出FOPL框架仅用输入与最终响应即可训练跨模型通用的隐藏CoT重构模型用于推理蒸馏
practical_value: '- 对接黑盒商用大模型做小模型蒸馏时，无需费成本调Prompt诱导CoT输出，可复用FOPL思路从大模型的最终响应还原推理链，降低蒸馏数据获取成本

  - Agent推理能力蒸馏场景下，无需依赖目标Agent的中间思考过程输出，仅用最终结果即可构造训练数据，适配黑盒商用Agent的蒸馏需求

  - 偏好对构造思路可迁移到推荐的用户路径建模：相同Query+点击Item下，将用户真实访问路径作为正样本、伪造路径作为负样本，训练更贴合用户行为的路径预测模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前前沿商用LLM大多隐藏CoT推理链以避免能力被蒸馏，现有CoT重构方法需要针对每个目标模型单独训练，泛化性差，黑盒大模型推理蒸馏成本极高，亟需一种模型无关的CoT重构方法，仅用输入和可见最终响应即可还原不同大模型的隐藏推理链。

### 方法关键点
- 提出Final-Output Preference Learning（FOPL）框架，基于DPO训练单一生成模型，无需输入目标模型身份信息即可适配不同大模型的推理风格
- 偏好对构造：针对同一问题，收集多个可访问CoT的源大模型的原生CoT和最终响应，再基于相同问题+最终响应生成合成CoT，将原生CoT作为偏好样本、合成CoT作为负样本构造DPO训练对
- 推理阶段重构模型仅需输入问题和目标大模型的最终响应，即可输出匹配目标模型推理风格的CoT

### 关键实验
用4个开源大模型的CoT数据训练4B参数的重构模型，测试覆盖训练见过的4个模型家族和未见过的MiMo模型：LLM-as-judge评估显示匹配目标模型响应的重构CoT相似度比跨模型高13~30个百分点，未见过的MiMo模型匹配率也达60.51%；用重构CoT训练1.5B学生模型，比仅用最终响应训练的学生在GSM8K上提升8.93pp、MATH-500上提升6.40pp，效果甚至优于原生CoT训练的学生；比SFT基线Trace Inversion方法在所有任务上领先10~20pp。

最值得记住的一句话：大模型的最终响应中已经携带了足够的推理风格信号，通过偏好学习可以有效还原隐藏推理链，无需依赖目标模型的中间输出即可实现高质量推理蒸馏。
