---
title: 'Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA'
title_zh: 短Chain-of-Thought在空间视觉问答中的失效机制：看得对却说错
authors:
- Chenhao Zhang
affiliations:
- Huazhong University of Science and Technology
arxiv_id: '2611.28665'
url: https://arxiv.org/abs/2611.28665
pdf_url: https://arxiv.org/pdf/2611.28665
published: '2026-11-20'
collected: '2026-11-24'
category: Reasoning
direction: 多模态推理 · CoT失效机制诊断
tags:
- Chain-of-Thought
- VLM
- Spatial VQA
- Reasoning
- LoRA
one_liner: 诊断15款开源+6款闭源VLM短CoT在空间VQA下的失效机制，验证答案步骤重接地能力可通过LoRA学习
practical_value: '- 多模态电商客服/商品问答Agent如果要引入CoT做空间类推理（如商品尺寸对比、摆放位置、前后遮挡类问题），不要默认CoT涨点，需先做小流量AB测试验证效果，避免中间步骤错误传导拉低准确率

  - 针对多模态CoT掉点场景，可复用闭源模型的答案步骤重接地设计，在输出最终答案前强制模型重新对齐原始视觉输入，避免被中间生成的错误推理文本锁死

  - 低成本修复多模态CoT失效可采用论文的LoRA微调方案，使用固定推理步骤+图像真值标签进行训练，无需全量微调即可让模型获得答案阶段重接地能力

  - 业务中涉及关系类CoT推理的场景，可加入中间步骤事实校验逻辑，一旦检测到中间生成内容与原始输入（图像/检索文档）矛盾，直接触发重推理，切断错误传导路径'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
短CoT在语言模型推理任务中普遍涨点，但在空间类视觉问答（VQA）任务中反而常导致准确率下降，此前对其失效原因的归因不明确，是多模态推理落地需要解决的核心问题。
### 方法关键点
- 测试覆盖15款2B~38B开源VLM（含普通指令微调、推理微调、大参数队列）、6款前沿闭源VLM
- 设计固定推理文本+孪生图像交换、逐句强制读out、中间关系编辑等对照实验，排除token长度、对话格式、视觉遗忘等干扰因素
- 结合中间层探针定位失效发生的具体阶段，拆解失效的核心来源
### 关键结果
- 80%的开源VLM CoT失效来自两类原因：57%为中间步骤输出错误空间关系，24%为中间关系正确但结论与问题映射错误
- 输出中间关系后，开源VLM的答案受图像的影响从直接回答时的20.5~76.5分骤降至2.0~8.9分，几乎完全被自身生成的文本锁死
- 3款头部闭源VLM无锁死问题，核心是在答案步骤会重新对齐图像信息；通过LoRA微调，开源VLM可学习到该重接地能力，修复自然图像场景的CoT失效问题
### 核心结论
短CoT在多模态感知类任务中的效果不升反降，核心原因是模型会优先信任自身生成的中间文本，而非原始输入的视觉信息
