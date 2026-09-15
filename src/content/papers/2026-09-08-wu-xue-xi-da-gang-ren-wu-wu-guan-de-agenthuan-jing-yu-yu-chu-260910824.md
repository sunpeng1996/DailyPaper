---
title: 'Studying Without a Syllabus: Task-Agnostic Environment Preprocessing'
title_zh: 无学习大纲：任务无关的Agent环境预预处理框架
authors:
- Vinay Samuel
- Varun Ursekar
- Vijay S. Kalmath
- Apaar Shanker
- Veronica Chatrath
- Yuan Xue
affiliations:
- Scale AI
- University of Maryland, College Park
arxiv_id: '2609.10824'
url: https://arxiv.org/abs/2609.10824
pdf_url: https://arxiv.org/pdf/2609.10824
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: Agent 无任务先验环境预处理优化
tags:
- LLM-Agent
- Task-Agnostic
- Preprocessing
- Environment-Adaptation
- Meta-Agent
one_liner: 无需下游任务先验，通过元Agent动态选择环境预处理策略，在6类异质基准上取得SOTA表现
practical_value: '- 冷启动场景可复用该任务无关预处理思路：新类目/新业务上线无标注数据时，提前通过元Agent构建环境索引、工具手册、领域技能库，降低下游推理成本

  - 预处理策略可做动态选型：根据环境属性（文档量级、工具复杂度）选择匹配方案，大文档场景优先CORPUS2SKILL，多工具场景优先PREPING或元Agent探索

  - 计算成本迁移可参考该框架：将多轮测试的重复计算转移到预任务预处理阶段，当预处理产物可复用超过10次时，总推理成本可降低1.6-5.5倍

  - 可构建企业级Agent预处理工具库：把常用的RAG构建、工具探索、技能蒸馏等流程做成可调用技能，供元Agent按需组合，减少重复开发'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent适配方法均依赖下游任务示例、轨迹或反馈信号，无法应对无任务先验的新环境冷启动场景；已有的任务无关预处理方案均为固定策略，仅适配单一类型环境（要么适合大语料场景，要么适合多工具交互场景），泛化性差。

### 方法关键点
- 正式定义任务无关环境预处理范式：预探索阶段无任何下游任务先验，仅在有限预算约束下探索环境，生成任意形态的可复用产物（索引、脚本、操作指南、知识库等）供固定求解器使用
- 提出两类META-AGENT变体：无辅助版本自主探索环境并生成适配产物；带归档库版本可调用内置的PREPING、CORPUS2SKILL等现有预处理工作流，按需组合生成最优产物
- 产物完全兼容现有Agent runtime，无需修改求解器的模型、prompt或工具调用逻辑

### 关键实验
在6类异质基准（含10万级文档检索、办公QA、法律知识库、多工具交互等场景）对比NOSTUDY、PREPING、CORPUS2SKILL基线：
- META-AGENT变体在5个基准上取得最高Avg@3 reward，带归档库版本在所有基准上排名前2
- 预处理可将测试阶段达到相同得分所需的采样次数减少2-8倍，单轮测试推理成本降低1.6-5.5倍，预处理成本可通过多轮复用摊销
- 预处理预算超过10美元后，多数场景下游效果无显著提升，预算收益边际递减明显

### 核心结论
任务无关预处理可将Agent的计算成本从重复的测试阶段转移到一次性的预探索阶段，动态适配的预处理策略比固定方案的泛化性和鲁棒性更强。
