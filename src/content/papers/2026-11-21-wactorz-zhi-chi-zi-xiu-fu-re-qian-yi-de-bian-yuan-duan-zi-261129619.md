---
title: 'Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the
  Edge'
title_zh: Wactorz：支持自修复、热迁移的边缘端自编写LLM Agent运行时
authors:
- Panagiotis Kasnesis
- Lazaros Toumanidis
- Amalia Contiero Syropoulou
- Christos Chatzigeorgiou
affiliations:
- Waldiez PC, Greece
- ThinGenious PC, Greece
arxiv_id: '2611.29619'
url: https://arxiv.org/abs/2611.29619
pdf_url: https://arxiv.org/pdf/2611.29619
published: '2026-11-21'
collected: '2026-11-24'
category: Agent
direction: 边缘端LLM Agent运行时优化
tags:
- LLM Agent
- Edge Computing
- Self-Healing
- Actor Model
- MQTT
one_liner: 提出开源边缘LLM Agent运行时，支持代码自生成、故障自修复、跨节点热迁移
practical_value: '- 借鉴Actor监督树+MQTT解耦架构，解决推荐系统多Agent编排的故障隔离问题，单个Agent崩溃不影响全链路，状态可持久化恢复

  - 复用Topic契约校验机制，解决多Agent（召回/排序/文案生成）间数据schema不匹配问题，无需预定义统一词汇表

  - 参考边缘热迁移逻辑，可将大模型推理Agent动态调度到空闲算力节点，降低电商大促时段核心服务的资源压力

  - 落地自修复逻辑：将运行时错误+traceback喂给LLM做代码原位修复，降低算法服务的人工运维成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent框架（AutoGen、CrewAI等）多为单脚本任务式运行，任务结束即终止，无法适配长期运行、容忍代码故障、边缘低算力部署的物理场景需求；传统边缘自动化工具则依赖静态人工规则，无法通过自然语言动态生成能力。
### 方法关键点
- 基于Erlang Actor模型+监督树设计，每个Agent为独立运行单元，崩溃时采用ONE_FOR_ONE策略单独重启，状态通过SQLite/序列化持久化，重启不丢失上下文
- 采用MQTT作为唯一协调层，Agent通过Topic而非名称寻址，Topic自动注册契约（生产者、消费者、payload采样），从根源避免多Agent间数据字段不匹配的经典问题
- 内置代码生成+自修复链路：PlannerAgent将自然语言请求转成Python代码生成DynamicAgent，运行时报错自动将代码+traceback喂给LLM做原位修复
- 支持边缘节点热迁移：Agent状态+依赖模型分片传输，哈希校验一致性，迁移后状态无中断
### 关键结果
Demo场景下，从自然语言请求生成摄像头检测→灯控自动化Agent，添加带除零错误的计数Agent，自动修复代码不丢计数，再热迁移到Raspberry Pi的全流程耗时小于4分钟，LLM调用总成本仅0.13美元。
### 核心结论
经典分布式系统的监督树+pub/sub解耦设计，是让LLM生成的不可靠代码能长期稳定运行的核心可行路径。
