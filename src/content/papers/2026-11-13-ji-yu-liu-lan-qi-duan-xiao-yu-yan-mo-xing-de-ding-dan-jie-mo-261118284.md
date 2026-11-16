---
title: 'Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model
  in Your Browser Tab'
title_zh: 基于浏览器端小语言模型的订单结构化静默错误检测
authors:
- Umar Ahmed
- Maxim Dunaev
- Mohammad Nour Al Awad
- Sergey Ivanov
- Ivan Khodnenko
affiliations:
- ITMO University
arxiv_id: '2611.18284'
url: https://arxiv.org/abs/2611.18284
pdf_url: https://arxiv.org/pdf/2611.18284
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: 端侧小模型 · 客户端LLM推理部署
tags:
- SLM
- WebAssembly
- On-device Inference
- Silent Error Detection
- Semantic Parsing
one_liner: 实现浏览器端运行的0.8B微调SLM，本地完成订单结构化与静默错误检测，无数据外泄
practical_value: '- 电商到店点餐、即时配送等订单语义解析场景可复用WebAssembly+llama.cpp端侧部署方案，用户输入全程不上传，满足隐私合规要求

  - 端侧SLM推理结果校验可复用「规则匹配+拒识兜底」机制，对不在预设候选集的输出返回?要求重输入，降低静默错误率

  - 端侧模型效果对齐测试可复用「端侧输出与服务端输出一致性校验」方法，本文0.8B模型99%的一致性可作为落地参考指标'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
将用户自然语言订单转为结构化票据的小模型存在两类错误：格式错误可被系统直接拦截，而格式合法但内容与用户需求不符的静默错误危害性高，同时传统服务端部署方案存在用户隐私泄露风险。
### 方法关键点
将微调后的0.8B参数小模型通过编译为WebAssembly的llama.cpp运行在用户浏览器端，订单数据全程不离开本地设备；同步将PIZZA基准匹配器移植为TypeScript版本在端侧运行，实时对生成的票据打分，对超出菜单范围的输入直接返回「?」拒识，支持用户交互测试静默错误。
### 关键结果
在1357条PIZZA测试订单上，端侧模型输出与服务端评估结果一致性达99.0%，Exact Match分数与服务端一致为0.882，同时公开了3款消费级笔记本上的推理latency数据。
