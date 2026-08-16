---
title: LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses
  in Autonomous Vehicles
title_zh: 大语言模型辅助自动驾驶软件攻击者可触达漏洞的动态威胁分析
authors:
- Md Wasiul Haque
- Sagar Dasgupta
- Mizanur Rahman
- Md Rayhanur Rahman
affiliations:
- The University of Alabama, Department of Civil, Construction & Environmental Engineering
- The University of Alabama, Department of Computer Science
arxiv_id: '2608.13450'
url: https://arxiv.org/abs/2608.13450
pdf_url: https://arxiv.org/pdf/2608.13450
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: LLM辅助软件漏洞动态分析
tags:
- LLM
- Dynamic Analysis
- Software Security
- Autonomous Driving
one_liner: 实证得出LLM辅助自动驾驶软件栈动态漏洞分析核心瓶颈为构建集成而非代码生成
practical_value: '- 做LLM代码生成类业务（如推荐系统策略代码自动生成、Agent工具代码生成）时，可借鉴编译器在环反馈+自动补全依赖的思路提升首次编译成功率

  - 分析LLM生成任务失败根因时，可参考本文的根因分类方法，优先解决占比80%的共性问题而非边缘逻辑问题

  - 若业务不涉及LLM辅助代码生成/安全分析，本文主要是自动驾驶安全领域学术贡献，可借鉴点有限'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
自动驾驶软件栈为安全关键系统，静态分析可识别候选漏洞点，但人工构造可执行测试用例验证可利用性成本极高，亟需自动化方案。

### 方法关键点
1. 对开源自动驾驶栈Autoware共185个包做编译器级精准静态分析，识别1375条决策规则、2274条校验规则、482条输入到安全输出流，采样740个可触达漏洞点；
2. 用2个本地开源LLM、无静态上下文消融组、朴素模板基线共生成3700组测试用例，接入编译器在环反馈修复，编译通过后做模糊测试。

### 关键结果数字
80%首次编译失败源于依赖配置而非程序逻辑；推理型LLM首次编译通过率达64%，远高于代码专用模型的6%；所有观测到的崩溃均来自桩代码而非Autoware本身，核心瓶颈为构建集成环节而非代码生成或模糊测试。
