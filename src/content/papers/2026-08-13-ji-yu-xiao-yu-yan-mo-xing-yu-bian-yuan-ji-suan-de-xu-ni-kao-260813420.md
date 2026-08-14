---
title: 'Enhancing Virtual Agents through SLMs and Edge-Computing: An Exploratory Evaluation
  of Think and Memory Processes'
title_zh: 基于小语言模型与边缘计算的虚拟Agent思考记忆能力探索评估
authors:
- Aimilios Hadjiliasi
- Louis Nisiotis
affiliations:
- University of Central Lancashire, Cyprus
arxiv_id: '2608.13420'
url: https://arxiv.org/abs/2608.13420
pdf_url: https://arxiv.org/pdf/2608.13420
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: 边缘端SLM驱动的虚拟Agent认知架构优化
tags:
- SLM
- Edge Computing
- Agent Memory
- Service Routing
- Embodied Agent
one_liner: 边缘部署不同规模Qwen2.5 SLM实现CEAA架构思考与记忆模块，验证性能-延迟权衡规律
practical_value: '- 端侧Agent选型可参考Qwen2.5系列的规模-性能-延迟数据：低延迟路由任务优先选1.5B版本，高准确率记忆任务选3B版本，资源极度受限场景不建议用0.5B以下SLM做核心逻辑

  - Agent的思考（路由）+记忆模块可采用轻量化拆分部署方案：路由模块用小SLM降低延迟，记忆读写模块用稍大SLM保障准确率，平衡整体性能

  - 结构化记忆落地可复用「SLM事实抽取+SQLite持久化+相关性/时效性召回」的轻量Pipeline，无需复杂RAG架构即可覆盖大部分单会话记忆需求

  - 边缘端SLM部署可优先采用Q4_K_M量化的GGUF格式，在Jetson这类低算力边缘硬件上也能实现秒级交互，满足非强实时场景需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
元宇宙/虚拟场景下的具身Agent需要低延迟、高隐私的本地认知能力，现有云侧LLM方案依赖网络、延迟高，传统规则式Agent又缺乏动态上下文适配能力，亟需探索边缘侧轻量SLM实现Agent核心认知模块（思考、记忆）的可行性与量化表现。

### 方法关键点
- 基于CEAA认知架构，将`Think`模块落地为多服务路由功能，`Memory`模块落地为结构化读写Pipeline，全链路部署在NVIDIA Jetson Orin NX 8GB边缘硬件
- 选用Qwen2.5 0.5B/1.5B/3B三个尺寸的指令微调模型，采用Q4_K_M量化、llama.cpp部署，上下文窗口设为4096token
- 记忆模块结合LangMem做事实抽取、SQLite做持久化，按会话ID+时间戳存储，读取时按相关性+时效性召回上下文
- 路由模块预设10类虚拟场景常用服务（对话、3D生成、语音合成等），要求SLM输出结构化JSON路由决策

### 关键实验
- 路由任务使用1000条人工标注prompt（每类服务100条）：1.5B模型准确率85.4%、平均延迟3349ms；3B模型准确率87.7%、平均延迟5067ms；0.5B模型仅29.4%准确率，不满足可用要求
- 记忆任务使用250组配对写-读prompt：3B模型端到端读准确率93.6%，1.5B为78.4%，0.5B为72.8%，但3B平均延迟达9693ms

### 核心结论
边缘端SLM驱动Agent核心认知模块时不存在通用最优选型，需根据任务对延迟/准确率的要求做模块化拆分部署
