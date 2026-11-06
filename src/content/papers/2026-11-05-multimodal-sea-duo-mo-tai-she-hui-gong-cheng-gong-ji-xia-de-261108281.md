---
title: 'Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering
  Attacks'
title_zh: Multimodal-SEA：多模态社会工程攻击下的AI Agent安全基准
authors:
- Zhitao He
- Chi Him Zhang
- Chengru Han
- Yi R Fung
affiliations:
- MMSense Lab, The Hong Kong University of Science and Technology
arxiv_id: '2611.08281'
url: https://arxiv.org/abs/2611.08281
pdf_url: https://arxiv.org/pdf/2611.08281
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: 多模态Agent安全 · 攻防基准构建
tags:
- Agent Security
- Multimodal Attack
- Benchmark
- Social Engineering
- Red Teaming
one_liner: 构建覆盖真实欺诈场景的多模态社会工程攻击AI Agent安全测评基准与框架
practical_value: '- 个人助理类Agent上线前可复用该基准的多模态欺诈场景做安全校验，降低被社工攻击的风险

  - 多模态Agent的安全防御不能仅依赖文本对齐的安全指令，需额外加入多模态伪造内容识别模块

  - 安全策略调优时需权衡攻击拦截率与合法请求拒绝率，避免影响用户正常使用体验

  - 红队测试时可复用论文的多模态攻击harness框架，实现可控的自适应攻击测评'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前个人AI Agent面临伪造多模态内容支撑的社会工程攻击威胁，但现有安全测评仅聚焦文本对话场景，多模态社工攻击下的Agent安全性缺乏系统评估。
### 方法关键点
1. 构建Multimodal-SEA交互式基准，包含608个基于真实欺诈案例的专家设计任务，覆盖14个领域、152种攻击场景，配套多模态攻击素材，分4个难度等级，适配中英文社会文化语境
2. 设计多模态攻击harness，整合任务信息、攻击进程控制、多模态内容生成能力，可实现可控红队测试，基于工具执行日志判定攻击结果
3. 从6个维度测评7款主流多模态模型的安全表现
### 关键结果
所有被测模型均存在漏洞，攻击成功率7.1%~34.5%；加入多模态内容后攻击成功率从19.9%提升至29.2%；强化安全指令仅能降低攻击成功率，无法提升对多模态欺诈内容的识别能力，部分低攻击成功率的模型存在过度拒绝合法请求的问题。
