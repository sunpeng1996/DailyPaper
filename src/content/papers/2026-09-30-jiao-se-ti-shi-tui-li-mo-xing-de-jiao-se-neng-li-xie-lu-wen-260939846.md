---
title: 'When a Kindergartener Solves Calculus: Measuring Capability Leakage in Role-Prompted
  Reasoning Models'
title_zh: 角色提示推理模型的角色-能力泄露问题测量与缓解方法
authors:
- Pakhapoom Sarapat
- Saksorn Ruangtanusak
- Kunat Pipatanakul
- Pittawat Taveekitworachai
affiliations:
- SCB DataX
- Nanyang Technological University
arxiv_id: '2609.39846'
url: https://arxiv.org/abs/2609.39846
pdf_url: https://arxiv.org/pdf/2609.39846
published: '2026-09-30'
collected: '2026-10-03'
category: LLM
direction: LLM角色提示 · 能力边界对齐
tags:
- Role Prompting
- Capability Leakage
- LLM Alignment
- Evaluation Benchmark
- Inference Intervention
one_liner: 提出ROLECAPBENCH基准检测角色能力泄露，给出推理时注入方案降低泄露
practical_value: '- 构建电商用户仿真Agent时，避免仅用基础角色提示模拟不同层级消费者，可复用本文Injection方案，给角色加明确能力边界+预填角色提醒前缀，解决能力泄露导致的仿真结果失真问题

  - 搭建分层级客服Agent时，用Syllabus+Injection组合方案，既能保证入门客服对基础咨询的回答准确率，又能降低超服务范围乱答的概率，减少客诉

  - 做生成式推荐的用户偏好模拟时，需先定义清晰的角色知识/能力边界，不要依赖LLM自发对齐人设，避免生成的偏好分布不符合真实用户画像'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有角色提示的评估仅关注话术风格、人设一致性，忽略了角色能力边界对齐问题：比如被设定为幼儿园学生的LLM能正确解答微积分题，这种角色-能力泄露（RCL）会导致用户仿真、角色扮演类Agent的输出完全失真，亟需可量化的评估基准和低成本的缓解方案。
### 方法关键点
- 构建ROLECAPBENCH基准，覆盖从小学到A-level的1568道标准化考试题，对应幼儿园到大学教师6种教育角色的明确能力边界
- 对比8种提示变体的RCL抑制效果，提出推理时干预方案Injection，结合显式角色能力规则+预填响应前缀，强制模型在回答前先确认自身角色能力边界
- 定义3个核心量化指标：符合角色能力的准确率（IA）、超角色能力的准确率（AA，数值越低泄露越少）、角色话术匹配度（RV）
### 关键实验结果
在Gemma-4-E4B、Qwen3.5-4B、OLMo-3-7B三个开源推理模型上测试：基础角色提示下AA高达0.811~0.898，RV得分1.218~1.389，说明模型话术符合角色但能力几乎完全泄露；Injection方案可将AA降低0.346~0.562，其中Gemma、Qwen的IA下降不超过0.058，兼顾角色能力对齐和正常回答能力。
### 核心结论
仅靠角色提示无法约束LLM的能力输出，可信的角色扮演Agent必须搭配显式能力边界定义和推理时干预措施
