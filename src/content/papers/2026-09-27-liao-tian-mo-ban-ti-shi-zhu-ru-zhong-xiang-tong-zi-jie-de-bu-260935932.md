---
title: 'Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template
  Prompt Injection'
title_zh: 聊天模板提示注入中相同字节的不同权限：保留Token表示的影响
authors:
- Yan Zhan
- Yunze Song
- Mengkai Hou
- Wanting Zhang
- Shaobo Liu
- Zhijun Gao
affiliations:
- Peking University
- National University of Singapore
- BYD Company Limited
- Shenzhen University
arxiv_id: '2609.35932'
url: https://arxiv.org/abs/2609.35932
pdf_url: https://arxiv.org/pdf/2609.35932
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: LLM Agent · 提示注入安全防护
tags:
- Prompt Injection
- LLM Agent
- Tokenizer
- Chat Template
- Security
one_liner: 验证LLM Agent提示注入攻击的权限大多来自保留token的学习表示而非文本本身
practical_value: '- 部署电商导购、运营类Agent时，可将工具返回、用户输入等非信任内容单独用移除了特殊token匹配逻辑的tokenizer编码，可直接降低39~66pp的模板伪造型提示注入攻击成功率

  - 设计Agent的角色/工具协议token时，不要将其配置为普通附加token，需纳入特殊token列表，避免标准防护漏判（当前255/400热门聊天模型存在该漏洞）

  - 涉及敏感操作的Agent（如下单、用户数据导出）可优先选择对保留token依赖强的模型（如Llama-3.1、GLM-4.5），拆分特殊token为子词即可实现低成本高收益的安全防护'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent的聊天模板伪造型提示注入攻击成功率极高，但既往研究无法区分攻击效果来自标记文本还是保留token的学习表示，标准tokenizer防护的覆盖范围也不明确，严重影响涉及用户数据、交易操作的电商、广告类Agent部署安全性。
### 方法关键点
- 控制输入字节完全一致，仅调整伪造聊天模板标记的编码方式：要么作为单保留control token输入，要么拆分为普通子词输入，完全排除文本差异的干扰
- 设计Matched对照组，在保留token编码的前提下额外增加和拆分操作等量的token，排除token数量变化对结果的影响，定义身份差Δ为两组攻击成功率的差值
- 覆盖单轮工具调用（InjecAgent）、多轮完整任务（AgentDojo）两类Agent基准，测试4个主流开源模型家族，同时审计Hugging Face Top400热门聊天模型的tokenizer配置
### 关键实验结果
- 单轮InjecAgent基准上，Llama-3.1、GLM-4.5、Seed-OSS-36B三个模型家族拆分保留token为子词后，攻击成功率下降39~66pp；仅Qwen3-8B因可通过推理识别文本标记，降幅仅8pp，抑制其推理块后降幅扩大到50pp
- 多轮AgentDojo基准上，身份差稳定存在；审计发现33/67种tokenizer配置（覆盖255/400热门模型）的工具协议token未被标准防护覆盖，仍存在攻击风险
- 自适应攻击者可通过寻找和保留token embedding接近的普通子词恢复攻击效果，但仍比无防护场景成功率低1.6~12.2pp
### 核心结论
提示注入攻击的权限跟随token表示而非文本字节，Agent防护必须面向输入token id设计，而非仅校验可见文本
