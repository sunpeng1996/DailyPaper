---
title: Stealing Reasoning Traces from Proprietary LLM APIs
title_zh: 从闭源大语言模型API窃取加密推理轨迹的攻击方法与风险研究
authors:
- Alexander Panfilov
- David Schmotz
- Ilia Shumailov
- Luca Beurer-Kellner
- Joachim Schaeffer
- Ameya Prabhu
- Jonas Geiping
- Maksym Andriushchenko
affiliations:
- MATS Research
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- Tübingen AI Center
- University of Tübingen
arxiv_id: '2608.09867'
url: https://arxiv.org/abs/2608.09867
pdf_url: https://arxiv.org/pdf/2608.09867
published: '2026-08-09'
collected: '2026-08-11'
category: LLM
direction: LLM安全 · 闭源API推理轨迹攻击
tags:
- LLM Security
- Reasoning Trace
- API Vulnerability
- Jailbreak
- Privacy Leakage
one_liner: 发现主流闭源LLM API加密推理块跨上下文兼容漏洞，可利用同厂商弱模型解码强模型的隐藏推理内容
practical_value: '- 业务侧使用闭源LLM搭建电商导购、推荐解释、客服等Agent应用时，公开或共享会话日志前必须剥离所有`thinking`/`signature`类加密推理字段，避免泄露用户PII、业务API密钥、内部策略等敏感信息

  - 存储Agent多轮会话数据时，不要明文存储加密推理块，要么落地前直接删除，要么使用业务侧独立密钥二次加密，防止第三方窃取后解码

  - 核心业务逻辑依赖闭源LLM推理能力（如商品定价、选品策略、用户偏好洞察）的团队，优先选择支持服务端存储推理状态、不返回加密推理blob的API版本，降低推理策略被窃取的风险

  - 做LLM应用合规审计时，需额外覆盖加密推理块的数据流：部分敏感信息可能不会出现在明文凭据与回复中，但会隐式存在于推理轨迹中，仅清理明文内容无法满足合规要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
主流闭源LLM厂商为保护知识产权、防范模型蒸馏，将模型内部Chain-of-Thought推理轨迹加密后以不透明blob形式返回给客户端，多轮会话时由客户端回传以避免服务端存储开销。此前仅发现加密块可跨会话复用，未系统性挖掘其潜在攻击风险与隐私泄露隐患。

### 方法关键点
- 验证同厂商加密推理块具备三重兼容性：跨会话、跨用户、跨同家族不同模型，例如Claude Opus生成的加密块可被同生态的Haiku模型正常识别加载
- 设计跨模型解码攻击：将强模型生成的加密推理块注入同厂商防护更弱的轻量模型，配合简单的转录prompt即可诱导弱模型输出明文推理内容，无需直接破解强模型的对齐防护
- 归纳四大攻击向量：专有推理能力蒸馏、第三方隐私数据提取、隐藏有害信息泄露、不可见prompt注入

### 关键结果
从GitHub、Hugging Face爬取6708条公开Agent会话日志，包含315320个加密推理块，解码后发现4.9%的会话存在敏感信息泄露，共提取到367条PII、182组凭证（含62个API密钥、33个密码）；攻击在Anthropic、OpenAI、Google三家主流厂商的API上全部验证有效，解码推理的token数与原模型上报的thinking token数高度匹配。

AI生态的安全强度由最薄弱的环节决定，哪怕是防护最严格的前沿模型，其泄露的加密推理轨迹也会被同生态的弱防护小模型破解，用户侧永远不能将加密推理块视为安全的存储介质。
