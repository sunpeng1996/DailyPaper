---
title: Code-Poisoning Property Inference Attacks
title_zh: 基于代码投毒的属性推断攻击方法
authors:
- Xukun Luan
- Yuhui Gong
- Gang Zhang
- Zixuan Huang
- Yuanguo Bi
- Xuesong Li
- Jinyan Liu
affiliations:
- Beijing Institute of Technology
- Northeastern University
arxiv_id: '2607.15970'
url: https://arxiv.org/abs/2607.15970
pdf_url: https://arxiv.org/pdf/2607.15970
published: '2026-07-17'
collected: '2026-07-20'
category: Other
direction: 机器学习隐私攻击 · 代码投毒
tags:
- Privacy Attack
- Code Poisoning
- Property Inference
- ML Security
- Supply Chain Attack
one_liner: 首个代码级属性推断攻击CPPIA，不降低模型精度即可实现100%攻击准确率
practical_value: '- 业务侧使用公开代码、Coding Agent生成的代码训练推荐/广告模型前，必须做代码审计，排查投毒风险，避免用户交易、行为等私有训练数据属性泄露

  - 对外发布模型推理API时，需增加异常请求检测，对批量查询罕见/未知样本的请求做限流拦截，防范属性推断攻击

  - 训练涉及敏感数据的模型时，优先使用经过安全验证的内部代码库，减少对GitHub等公开代码、第三方代码生成工具的依赖'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前开发者大量依赖GitHub公开代码、Codex等编码Agent快速构建ML模型，训练数据（如电商交易记录、用户行为数据）全局属性泄露风险高，现有属性推断攻击存在准确率低、损害模型精度、计算开销大、易被防御等缺陷。
### 方法关键点
提出首个代码级属性推断攻击CPPIA，恶意代码提供者在公开代码中植入投毒逻辑，数据持有者使用中毒代码训练私有模型时，攻击逻辑会将训练集属性嵌入秘密样本特征中，攻击者仅需通过模型公开的标签API查询这些秘密样本即可窃取训练集全局属性，无需训练影子模型，计算开销极低。
### 关键结果
在4个数据集、8种模型架构、18种属性、3种防御机制下验证，CPPIA攻击准确率达100%，且完全不降低原有模型的推理精度，普适性极强。
