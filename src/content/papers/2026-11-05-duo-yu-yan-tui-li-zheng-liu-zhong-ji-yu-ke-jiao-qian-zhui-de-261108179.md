---
title: 'Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning
  Distillation'
title_zh: 多语言推理蒸馏中基于可教前缀的动态教师监督方法
authors:
- Jaewon Cho
- Minseo Yoon
- Jinyoung Park
- Jinwoo Seo
- Jaewon Chu
- Alice Oh
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2611.08179'
url: https://arxiv.org/abs/2611.08179
pdf_url: https://arxiv.org/pdf/2611.08179
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 大模型训练 · 多语言推理自蒸馏优化
tags:
- Knowledge Distillation
- Self-Distillation
- Multilingual Reasoning
- LLM Training
- Teacher Drift
one_liner: 提出TOPSD动态选择可教前缀并验证教师可恢复性，解决多语言推理自蒸馏的教师漂移问题
practical_value: '- 做垂域LLM微调/蒸馏时，可借鉴可教前缀选择思路，仅在教师仍能纠正错误的前缀段施加监督，避免错误累积导致的训练退化，尤其适配低资源垂域、小语种场景的模型训练

  - 可引入教师可恢复性校验机制，对每条生成轨迹先验证教师能否从当前前缀推导正确结果，仅对校验通过的样本做蒸馏，大幅降低噪声样本对训练的干扰

  - 跨境电商多语言Agent推理能力训练可复用TOPSD框架，用高资源语言的参考答案作为特权信息，显著提升低资源语言的推理准确率，适配多语言客服、营销文案生成等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）无需额外大教师模型，仅用同模型加参考答案作为特权教师即可提升推理能力，但扩展到多语言场景时会出现**Teacher Drift**问题：学生生成的错误前缀累积后，教师会放弃纠正转而跟随学生的错误推理，且低资源语言中漂移出现更早，导致蒸馏效果大幅下降。
### 方法关键点
- 可教前缀选择：计算累积教师-学生似然比，当比值连续K次超过阈值τ时判定为漂移起始点，仅保留该点前的前缀作为候选监督段
- 教师可恢复性验证：让教师基于选中的前缀生成后续推理，验证是否能得到正确答案，仅验证通过的前缀参与蒸馏
- 损失优化：对参与蒸馏的token做语言级、轨迹级归一化，平衡不同资源语言的训练权重，全程保留OPSD的on-policy特性，不用教师生成内容作为训练目标
### 关键实验
在10种语言的OpenThoughts数据集上训练，在PolyMath High测试集对比Vanilla、OPSD、COPSD基线，覆盖Qwen3-1.7B/4B/8B三个规模：TOPSD的Avg@3分别达11.60%/17.79%/25.12%，比最强基线提升1.65/1.07/2.64个百分点；低、中资源语言提升更显著，8B模型在中资源语言上Avg@3提升3.47个百分点。
### 核心结论
可靠的on-policy自蒸馏不仅需要强教师，更需要知道教师什么时候还能有效教学、其指导是否可信
