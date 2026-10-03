---
title: Replacing Large Language Models with Jev Decision Models for Low-Latency Edge
  Service Orchestration
title_zh: Jev决策模型替代大模型实现低延迟边缘服务编排
authors:
- Delong Li
- Xu Wang
- Haochen Gong
- Rui Lang
- Guangsheng Yu
affiliations:
- University of Technology Sydney
arxiv_id: '2609.22753'
url: https://arxiv.org/abs/2609.22753
pdf_url: https://arxiv.org/pdf/2609.22753
published: '2026-09-25'
collected: '2026-10-03'
category: LLM
direction: 低延迟决策 · LLM替代方案
tags:
- Decision-Model
- LLM-Substitution
- Latency-Optimization
- Service-Orchestration
- Edge-Computing
one_liner: 提出用Jev专用决策模型替代通用LLM做服务编排决策，降延迟减成本提升高负载可用性
practical_value: '- 强延迟约束的固定格式决策场景（如电商实时营销准入、搜索意图快速分类）可参考限定意图字段+共享校验器的轻量架构，替代通用LLM大幅降低决策延迟

  - 高流量高峰时段的核心决策链路，可采用专用决策模型兜底通用LLM，在可接受的精度损失下保障服务可用性，避免因LLM超时导致业务损失

  - 固定契约格式的批量决策场景可试点专用决策模型替代通用LLM，单决策成本可降低60%以上，大幅压缩调用成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
边缘侧自然语言服务请求需先经LLM完成决策再执行，大量占用延迟预算，高负载下LLM服务可用性骤降，API调用成本也居高不下。
### 方法关键点
将Jev决策专用API集成到边缘服务编排链路，提取4-8个边界明确的意图字段，搭配共享校验器、准入策略、调度器，全链路纳入请求决策等待耗时统计与优化。
### 关键结果数字
33组测试条件下，Jev相对最快LLM中位数决策延迟降低22.7%~64.5%，延迟不受输入大小、契约宽度、服务目录规模影响；4字段契约场景下，单正确决策API费用降低59.7%~80.9%，仅损失少量精确匹配率；高负载场景下LLM按时准确率低于0.1时，Jev仍保持0.91~0.95的按时精确请求占比，核心优势体现在无缓存的新鲜决策场景。
