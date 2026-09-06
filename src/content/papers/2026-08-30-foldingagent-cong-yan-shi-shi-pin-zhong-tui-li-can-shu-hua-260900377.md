---
title: 'FoldingAgent: Inferring Parametric Origami Procedures from Demonstration Videos'
title_zh: FoldingAgent：从演示视频中推理参数化折纸操作流程
authors:
- Maya Moriya
- Sigal Raab
- Yael Vinker
- Tali Dekel
affiliations:
- Weizmann Institute of Science, Israel
- MIT, USA
arxiv_id: '2609.00377'
url: https://arxiv.org/abs/2609.00377
pdf_url: https://arxiv.org/pdf/2609.00377
published: '2026-08-30'
collected: '2026-09-06'
category: Agent
direction: 多模态Agent · 视频转可执行结构化指令
tags:
- VLM
- Agent
- Tool Use
- Multimodal Reasoning
- Video Understanding
one_liner: 提出VLM+专用工具的Agent框架，将折纸演示视频转换为可执行参数化折叠程序
practical_value: '- 多模态Agent结合领域专用工具+仿真校验的架构，可复用在电商场景下从DIY/手工教程视频自动提取可执行步骤，生成导购内容素材

  - 多步任务引入重规划机制缓解误差累积的思路，可迁移到长序列用户行为建模、多轮推荐会话的路径规划场景

  - 定义领域参数化空间将非结构化视觉内容转结构化可执行指令的范式，可用于直播/短视频商品卖点自动结构化提取'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有折纸计算方法依赖结构化折痕图案/参数化计划，而人类折纸知识大多以非结构化演示视频形式传播，二者存在明确 gap；传统多步预测模型易出现误差累积问题，生成的结果不可执行。

### 方法关键点
1. 基于预训练VLM搭建Agent框架，搭配几何过渡仿真、物理合理性校验、视觉内容检索比对、自评估4类专用工具
2. 定义包含纸张几何属性、参数化折叠动作的专属参数空间，实现视觉内容到折叠程序的映射
3. 采用序列决策+动作重规划机制，缓解多步折叠任务固有的误差累积问题

### 关键结果
在新构建的带几何与动作真值标注的PurelandFold基准数据集上验证，可成功将非结构化视频演示转换为可执行、物理合理的折叠流程
