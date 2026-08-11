---
title: 'Thinking With Tools, Not With Pixels: Tool Calls as Text Scaffolds for Visual
  Reasoning'
title_zh: 借助工具而非像素推理：工具调用作为视觉推理的文本支架
authors:
- Jiahao Shao
- Yuanbo Yang
- Yiyi Liao
- Yujun Shen
- Ceyuan Yang
- Yinghao Xu
affiliations:
- Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
- Ant Group
- Zhejiang University
arxiv_id: '2608.09682'
url: https://arxiv.org/abs/2608.09682
pdf_url: https://arxiv.org/pdf/2608.09682
published: '2026-08-10'
collected: '2026-08-11'
category: Reasoning
direction: 多模态视觉推理 · 工具调用范式优化
tags:
- VLM
- Tool Calling
- Visual Reasoning
- Latency Optimization
- Scaffold Learning
one_liner: 提出无像素返回的TextCall范式，仅靠工具调用文本支架实现同等视觉推理效果，延迟降29-46%
practical_value: '- 电商多模态Agent（商品图问答、直播内容识别、AI导购场景）可直接复用TextCall思路，裁剪工具返回的图像解析环节，仅保留调用意图、坐标文本支架，在保证效果的前提下大幅降低推理延迟

  - 训练工具增强的多模态模型时，可拆分工具调用的「意图推理文本+空间坐标」两个组件，针对场景优化标注：高分辨率商品细节识别侧重坐标标注，通用商品属性问答侧重意图文本标注，降低标注成本

  - 部署侧可先对业务场景做像素必要性校验，大部分感知类多模态任务无需保留工具返回的像素流，省掉图像预处理、第三方工具API调用开销，实测 latency 最高降46%'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有工具增强视觉语言模型（VLM）默认返回像素是视觉推理的核心输入，但大量诊断实验发现返回像素对性能贡献极低，性能增益的真实来源不清晰，同时图像返回带来额外的推理延迟、工具API调用开销，推高工程落地成本。

### 方法关键点
- 提出TextCall（call-but-no-return）范式，训练和推理阶段均完整保留工具调用的结构化文本支架（工具名称、操作坐标、目标描述、执行意图），仅将工具返回的图像替换为固定文本占位符`[Image output skipped]`，完全消除对返回像素的依赖
- 设计三组对照实验验证工具调用支架假说：非必要性测试对比有无像素返回的性能差异，充分性测试对比仅支架输入和仅图像输入的准确率，组件拆分测试验证推理文本、空间坐标各自的贡献

### 关键结果
以Qwen2.5-VL-7B为基座，在V*Bench、HR-Bench等11个视觉推理基准上测试，对比标准带图像返回的thinking-with-images范式：
1. LoRA/全参数微调阶段，TextCall性能匹配甚至超过原范式，9.5K数据量下V*Bench准确率高5.23pp，65K数据量下6个核心基准平均高1.39pp
2. RL训练阶段，TextCall稳定保持75%的工具调用率，原范式直接崩溃放弃工具调用
3. 部署端到端延迟降低29-46%，完全消除工具执行API调用开销

### 核心结论
当前主流视觉推理任务分布下，工具调用的结构化文本支架才是承载性能增益的核心，返回像素大多是可移除的冗余载体
