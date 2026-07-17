---
title: 'CoTu at EXACT 2026: Neuro-Symbolic Reasoning for Transparent Educational QA'
title_zh: EXACT 2026 CoTu队方案：面向透明教育QA的神经符号推理
authors:
- Quoc-Khang Tran
- Minh-Thien Nguyen
- Phu-An Thai
- Xuan-Tung Bui
- Truong-Thanh Ma
- Nguyen-Khang Pham
affiliations:
- Can Tho University, Vietnam
- Tay Do University, Vietnam
arxiv_id: '2607.14735'
url: https://arxiv.org/abs/2607.14735
pdf_url: https://arxiv.org/pdf/2607.14735
published: '2026-07-16'
collected: '2026-07-17'
category: Reasoning
direction: 神经符号推理 · 小模型可解释QA
tags:
- Neuro-Symbolic-Reasoning
- Program-of-Thought
- Small-LLM
- Explainable-AI
- Z3-Solver
one_liner: 基于4B小模型的神经符号思维链编程框架，实现可验证高准确率可解释教育QA
practical_value: '- 小模型规则类推理可复用「生成可执行代码→符号求解器验证」范式，规避幻觉，同时生成可解释推理路径，适合电商售后/活动规则查询、合规校验场景

  - SGLang+投机解码+蒸馏微调的低延迟小模型服务栈，可直接迁移至高并发、小算力部署的推理场景，如实时客服QA、推荐理由生成

  - 任务路由+统一结构化输出+自校正循环的框架，可复用在需要可验证结果的Agent任务中，如营销活动规则自动核验、选品合规校验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
可解释教育QA要求答案既准确又具备可解释性，EXACT 2026竞赛限定仅可使用8B参数以下开源自托管模型，无法依赖大闭源模型的推理能力，设置了高校规则逻辑推理、多步骤物理题求解两类任务。
### 方法关键点
采用神经符号Program-of-Thought流水线：4B参数基座不直接输出答案，规则类查询生成Z3编码交由求解器做蕴含判定，物理题生成数值Python代码执行；配套统一自校正循环、可解释JSON输出结构，搭配答案类型路由、蒸馏微调、SGLang+投机解码的低延迟服务栈，单query耗时控制在60s内。
### 关键结果
物理任务所有自动化选拔轮次满分，决赛技术分全场最高13.44/15（结合自动答案评估+专家推理深度评分），总排名第3；验证小模型结合符号求解器可实现正确可验证的推理，当前瓶颈在前提选择而非推理本身。
