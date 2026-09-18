---
title: A Scalable Trust Discovery Architecture for the Internet of Agents
title_zh: 面向Agent互联网的可扩展信任发现架构
authors:
- Song Zhang
- Jiankang Yao
- Hongtao Li
- Xiaojun Zhang
- Xugang Shen
- Xin Li
- Yanbiao Li
affiliations:
- 中国互联网络信息中心
- 阿里云智能集团
- 互联网域名管理技术国家工程实验室
- 中国科学院计算机网络信息中心
arxiv_id: '2609.20095'
url: https://arxiv.org/abs/2609.20095
pdf_url: https://arxiv.org/pdf/2609.20095
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 跨平台可信发现基础设施
tags:
- Internet of Agents
- Trust Discovery
- Multi-agent System
- Identity Management
- Distributed Architecture
one_liner: 提出DNS启发的三层Agent信任发现架构，实现高吞吐低延迟的可信Agent身份管理与能力发现
practical_value: '- 搭建内部多Agent协作平台时可复用三层Root-Registry-Resolver架构，无需从零设计可信发现逻辑，适配电商导购、客服、运营等多Agent跨域协作场景

  - 可借鉴注册后缀锚定的复合身份方案，给内部自研Agent、第三方接入Agent生成全局唯一可验证身份，避免身份仿冒风险

  - 双证书多级认证机制可直接复用在Agent调用链路，根据场景选认证等级：低风险内部Agent调用用基础认证，高风险支付类Agent调用用高级认证，平衡效率与安全

  - 性能指标可作为自建Agent发现服务的参考基准：注册延迟≤60ms、发现延迟≤30ms、QPS≥万级即可满足大中台级Agent调度需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent协议多聚焦工具调用、跨Agent通信，缺乏可扩展的注册、可信身份校验、能力导向的发现机制，大规模跨平台Agent生态下，存在身份难验证、能力匹配效率低、恶意仿冒等风险，无法支撑Agent互联网的可信协作需求。

### 方法关键点
- 借鉴DNS分层设计，采用三层分布式架构：Agent Root作为全局信任锚管理授权注册商，Agent Registry负责Agent注册与元数据发布，Agent Resolver提供分布式能力发现与信任感知解析
- 设计注册后缀锚定的复合身份方案，将Agent原生标识与可信注册商后缀绑定，生成全局可发现的兼容DNS格式的身份
- 双证书多级认证机制：私有CA支撑域内高效信任建立，公有CA支撑跨域可信互联，同时设基础、增强、高级三级认证适配不同安全等级场景
- 结构化发布Agent能力卡与信任卡，Resolver侧基于本地索引实现信任感知的能力检索

### 关键实验结果
基于自研ATI原型系统测试，单节点部署下平均注册延迟58ms，平均发现延迟25ms，支持1.9万+注册QPS、2.9万+发现QPS，性能满足大规模部署需求。

### 核心结论
Agent生态的规模化落地，不仅需要通信协议，更需要基础设施级的可信发现与身份治理体系。
