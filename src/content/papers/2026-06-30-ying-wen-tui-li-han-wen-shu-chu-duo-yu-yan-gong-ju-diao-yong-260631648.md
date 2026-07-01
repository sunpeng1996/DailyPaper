---
title: 'Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using
  Agents'
title_zh: 英文推理韩文输出：多语言工具调用Agent的高效适配方案
authors:
- Utsav Garg
- Sungjin Hong
- Jason Jung
- Justin Lee
- Shaan Desai
- Joon Hee Kim
- Anirudh Shrinivason
- Edmond Wen
- Susie Park
affiliations:
- Cohere
- LG CNS
arxiv_id: '2606.31648'
url: https://arxiv.org/abs/2606.31648
pdf_url: https://arxiv.org/pdf/2606.31648
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 多语言工具调用Agent低成本适配
tags:
- Tool-using Agent
- Multilingual LLM
- RLVR
- DPO
- 4-bit Quantization
- SFT
one_liner: 基于成熟通用大模型三阶段适配111B双语工具Agent，支持单H100 4bit部署，推理工具能力远超基线
practical_value: '- 多语言Agent可采用「通用语内部推理+用户语言输出」架构，无需强行适配小语种推理，大幅降低训练成本，比如跨境电商Agent可英文调用库存/订单工具，本地语言输出结果

  - 工具调用能力适配可走「SFT冷启动（best-of-N拒绝采样构造合格样例）+ RLVR可验证奖励优化 + 低学习率DPO修正风格」三阶段pipeline，避免RL冷启动无奖励信号问题，适配电商NL2SQL、优惠券/订单查询等工具场景

  - 大参数企业级Agent可直接采用4-bit量化部署，111B模型仅损失不到3%的推理/工具能力即可单H100运行，大幅降低推理成本，适合业务侧中小流量的专用Agent部署

  - 可通过preamble conditioning让同一模型支持「推理/非推理」双模式，推理模式用于工具调用、复杂计算，非推理模式用于普通对话回复，不用部署多套模型，降低运维成本'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
企业级多语言Agent部署需同时满足工具调用准确率、多语言一致性、低显存占用要求，从头训练大模型成本极高，通用预训练大模型的工具调用、小语种适配能力不足，大参数模型部署显存成本过高，亟需低成本的成熟大模型适配方案。
### 方法关键点
- 三阶段适配pipeline：基于已完成后训练的Cohere Command A 111B通用模型，先后经过混合SFT、RLVR、低学习率DPO偏好对齐，无需重新预训练
- 双模式推理设计：通过preamble conditioning切换工作模式，推理模式输出英文中间推理链适配工具调用、NL2SQL等任务，非推理模式直接输出简洁用户回复；针对小语种输入，强制最终回复匹配用户语言，中间用英文推理解决小语种推理信号不足问题
- RLVR阶段新增语言一致性惩罚，输出语言与输入不匹配扣0.5奖励，解决多语言场景下输出漂移问题
- 4-bit量化压缩模型，显存占用减半，支持单80GB H100部署
### 关键结果
对比Command A、GPT-4o、Claude 3.7 Sonnet等基线，Enterprise NL2SQL准确率从7.3提升至38.0，LG Agentic Eval得分从2.67提升至4.85，韩语输出漂移率从12.2%降至0.8%，4-bit量化后能力损失<3%，通用多语言指令跟随能力保留98%以上。
最值得记住的一句话：多语言工具Agent无需强制适配小语种全链路推理，分离内部推理语言与用户输出语言可大幅降低适配成本。
