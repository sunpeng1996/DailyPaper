---
title: 'OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory'
title_zh: OpenVLHarness：支持多模态记忆的真实场景视觉智能体工具调用框架
authors:
- Yu Zhou
- Cheng-Fu Yang
- Rui Sun
- Di Wu
- Sibo Peng
- Mingyang Zhang
- Zhen Yang
- Ruiyi Zhang
- Nanyun Peng
- Zhe Gan
affiliations:
- University of California, Los Angeles
- Apple
arxiv_id: '2610.26860'
url: https://arxiv.org/abs/2610.26860
pdf_url: https://arxiv.org/pdf/2610.26860
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 多模态Agent 工具调用与记忆优化
tags:
- Multimodal Agent
- Tool Use
- Multimodal Memory
- MLLM
- Visual Reasoning
one_liner: 提出融合能力层与多模态持久化记忆的视觉智能体工具调用框架，无需微调即可大幅提升多模态任务表现
practical_value: '- 可复用工具层设计：将OCR、视觉定位、搜索等异构工具封装为统一任务级接口，上层Agent无需修改调用逻辑即可替换工具后端，适配电商商品属性提取、商品识别等多工具调度场景

  - 多模态记忆设计：将图片、结构化数据、检索结果按可复用句柄存储，每轮仅向MLLM推送句柄列表无需传输全量数据，可大幅降低多轮交互场景（如智能导购Agent）的Token成本

  - 工具输出渲染机制：将工具返回的掩码、深度数组等非结构化数据转换为「可视化附件+短文本描述+结构化字段」的MLLM可读格式，无需微调即可提升MLLM理解工具输出的准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MLLM在复杂视觉推理任务（如密集物体计数、空间距离测量、长尾实体信息查询）上仅靠提升推理预算收益极低，2.7倍推理Token投入仅带来0.7个点的效果提升；现有视觉工具调用框架存在异构工具接口不统一、输出格式MLLM难以理解、多轮调用时工具结果无法复用的痛点。

### 方法关键点
- 核心架构分为能力层+多模态持久化记忆两层，上层为MLLM编排器，全程无需微调基座模型
- 能力层：封装9类标准化任务级工具接口（视觉定位、OCR、深度估计、文本/图像搜索、代码执行等），统一异构工具的调用方式；内置证据渲染模块，将工具输出的掩码、数值数组等转换为「可视化附件+短文本描述+结构化字段」的MLLM可读格式
- 多模态持久化记忆：按图片、结构化数据、网页引用三类存储所有工具输出，分配可复用句柄，每轮仅向MLLM推送可用句柄列表，无需重复传输全量数据；支持基于记忆的代码执行，可跨多工具结果做聚合计算

### 关键实验
在22个多模态基准（覆盖感知、搜索、VQA、空间推理4大类）上测试8款开源/闭源MLLM，对比无工具基线、OctoTools、Visual Sketchpad、Codex等现有方案：
1. 相对无工具基线平均得分提升9.7~12.6个百分点，其中Qwen3-VL-8B提升11.2，Kimi K3提升9.7，GPT-6 Astra提升9.9
2. GPT-6 Luna中等推理力度下，效果比最大推理力度的基线、Codex、Visual Sketchpad高7.7~8.5个百分点，仅消耗其37%的Token成本

### 核心结论
推理预算的边际收益极低，为MLLM搭配标准化工具调用层和可复用多模态记忆，是提升复杂多模态任务效果的更高效路径。
