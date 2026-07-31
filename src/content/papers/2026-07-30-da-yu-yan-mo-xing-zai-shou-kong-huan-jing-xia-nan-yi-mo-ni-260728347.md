---
title: LLMs struggle to simulate human belief updates in controlled environments
title_zh: 大语言模型在受控环境下难以模拟人类信念更新过程
authors:
- Sebastian Pohl
- Harsh Mehta
- Pranav Mambayil
- Abdul Ghafoor
- Franziska Lesigang
- Yufang Hou
- Christian Hilbe
affiliations:
- IT:U, Interdisciplinary Transformation University Austria
arxiv_id: '2607.28347'
url: https://arxiv.org/abs/2607.28347
pdf_url: https://arxiv.org/pdf/2607.28347
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: 大语言模型 · 人类行为模拟可信度验证
tags:
- LLM
- Human Behavior Simulation
- Belief Update
- Bias Analysis
- Persona
one_liner: 通过6款LLM与391名人类受试者的信念更新对比实验，明确LLM模拟人类信念动态的适用边界
practical_value: '- 做用户观点演化、舆情传播仿真类Agent时，必须锚定真实用户初始立场数据，仅靠人口属性、人格标签生成的初始状态偏差极大

  - 用LLM做商品评论说服力排序、用户态度迁移预测时，需针对性修正LLM天生的「中立偏好过强、态度偏移幅度过小」两类系统偏差

  - 多轮社交内容传播、用户舆论干预仿真类项目，不能完全依赖LLM自生成的初始用户 stance，否则结果可信度无法保障'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM被广泛用作社会科学实验、社交动态仿真的人类受试者代理，该做法的保真度缺乏系统性验证，同类需求也大量存在于用户建模、舆情预判等业务场景。
### 方法关键点
选取6款主流LLM，基于391名英国受试者的人口属性、人格标签构建persona，一对一模拟受试者阅读Reddit评论前后的观点更新过程，与人类真实标注数据做1:1对标。
### 关键结果
仅Qwen3-32B、GPT-5-Mini在输入人类真实初始立场时，输出的后续立场分布与人类一致；所有模型均无法自行生成符合人类分布的初始立场，也无法基于自生成立场输出可信的信念更新。
全量模型存在三类共性偏差：中立立场占比过高、态度更新频繁但幅度远小于人类、无法正确排序评论的说服力；仅输入人口/人格标签对模拟保真度无稳定提升。
