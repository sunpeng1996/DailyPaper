---
title: 'SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident
  Response'
title_zh: SecRespond：真实入侵后事件响应场景的AI Agent评测基准
authors:
- Lehan Wang
- Boli Chen
- Ruixue Ding
- Pengjun Xie
- Jinwei Huang
- Zhendong Liu
- Shuo Wang
- Tao Lei
- Xin Ouyang
- Xiaomeng Li
affiliations:
- Tongyi Lab, Alibaba Group
- Alibaba Cloud Computing, Alibaba Group
- The Hong Kong University of Science and Technology
arxiv_id: '2607.26791'
url: https://arxiv.org/abs/2607.26791
pdf_url: https://arxiv.org/pdf/2607.26791
published: '2026-07-28'
collected: '2026-08-02'
category: Agent
direction: AI Agent 网络安全场景评测
tags:
- Agent
- Benchmark
- LLM
- Cybersecurity
- Evaluation
one_liner: 首个针对入侵后事件响应流程的LLM Agent评测基准，覆盖10个真实云主机构建的网络靶场
practical_value: '- 做垂直领域Agent评测可复用这套构建逻辑：先明确定义任务输出范式，再基于真实业务场景构造多维度测试用例，避免理想环境评测和实际表现脱节

  - 开发需主动探索+闭环决策的垂直Agent（如电商异常订单审计、客诉根因排查Agent）时，需重点优化无提示下的主动信息挖掘能力、输出结果的可验证性，对齐本次发现的LLM
  Agent通用瓶颈

  - 企业内部运维/安全类Agent可直接使用该开源基准测试能力，无需从零搭建入侵响应场景测试集'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有网络安全领域LLM Agent评测均聚焦攻击发生前的干净理想环境，入侵后的事件响应场景评估严重缺失，无法验证Agent在真实受损主机场景下的排查与修复能力。
### 方法关键点
构建SecRespond基准，给定受损主机的取证磁盘快照、安全产品告警、漏洞扫描与基线检查结果，要求Agent输出入侵取证报告、基线/漏洞风险评估、修复方案；基准覆盖10个由真实受损云主机构建的网络靶场，横跨4类入侵入口、21种ATT&CK技术、5种操作系统，基于OpenCode Agent框架测试23个前沿LLM的表现。
### 关键结果
现有Agent仅能可靠识别告警明确暴露的问题，在无提示下主动挖掘静默入侵、生成可验证的完整修复方案表现极差，无任何模型能在任意1个靶场中实现100%的检测与修复。
