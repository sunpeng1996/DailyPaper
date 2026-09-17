---
title: Clueing up LLMs with Tool-Augmented Deductive Reasoning
title_zh: 工具增强演绎推理提升大语言模型多轮交互推理能力
authors:
- Rebecca Ansell
- Autumn Toney-Wails
affiliations:
- Georgetown University
- Syntheos, Corp
- UNU-MERIT
arxiv_id: '2609.18736'
url: https://arxiv.org/abs/2609.18736
pdf_url: https://arxiv.org/pdf/2609.18736
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent工具增强 · 演绎推理优化
tags:
- LLM Agent
- Tool Augmentation
- Deductive Reasoning
- Multi-Agent Environment
- State Tracking
one_liner: 在Clue多智能体桌游环境验证外部结构化信念跟踪工具可大幅提升LLM多轮演绎推理能力
practical_value: '- 电商多轮导购/客服Agent可复用结构化状态跟踪思路，将用户历史交互、偏好、上下文约束编码为结构化状态矩阵，替代纯自然语言上下文传递，降低LLM记忆错误率，减少上下文长度开销

  - 推荐系统用户动态兴趣跟踪可借鉴可能性矩阵增量更新逻辑，对不同候选集的匹配概率做显式YES/NO/MAYBE标记，基于实时交互自动更新约束，提升兴趣推断准确率

  - 多智能体协作场景（如广告投放策略群智优化）中，少量工具增强Agent即可带动整体群体决策质量，无需全链路改造即可获得显著收益，可优先在核心节点部署工具增强能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM在多轮长交互场景下难以维持逻辑一致的演绎推理，现有静态推理基准无法衡量跨多步依赖的信念状态一致性，现有工具增强方案要求模型自主判断工具调用时机，在复杂交互场景下落地难度高，亟需轻量、无需模型自主调参的推理增强方案。
### 方法关键点
- 搭建基于经典桌游Clue的多智能体测试环境，6个Agent（3个GPT-4o-mini、3个Gemini-2.5-Flash）轮流出牌，需基于部分观测推断隐藏的嫌疑人、凶器、地点组合，模拟多轮演绎推理场景
- 设计结构化可能性矩阵工具，显式存储每张卡牌的归属状态（YES/NO/MAYBE），自动基于公共交互、私有观测增量更新约束，无需Agent自主调用，每轮自动注入prompt作为权威状态参考
- 设置三组对照实验：全基线Agent组、全工具增强Agent组、混合组（1个工具增强+2个基线Agent per模型族），从指控准确率、推理质量、知识积累效率、决策延迟四个维度评估效果
### 关键结果
- 全基线组指控准确率仅0.24~0.3，无Agent能完全猜对答案；全工具增强组Gemini-2.5-Flash准确率达100%，GPT-4o-mini准确率达96%，整体94.5%的Agent完全猜对答案
- 混合组中无工具的基线Agent准确率从0.81/3提升到2.71/3，工具增强Agent的高质量公共决策会带动全局群体性能
- 工具增强Agent无需积累全量信息即可做出正确决策，平均推理轮次比基线Agent缩短近一半

> 最值得记住的结论：将长交互场景下的信念跟踪从LLM内部记忆卸载到外部结构化工具，是轻量提升多轮演绎推理性能的高性价比方案，无需微调或复杂工具调用能力即可落地
