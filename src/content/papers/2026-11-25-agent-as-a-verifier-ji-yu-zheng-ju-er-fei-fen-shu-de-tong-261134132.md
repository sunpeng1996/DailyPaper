---
title: 'Agent-as-a-Verifier: From Scores to Evidence for General Verification'
title_zh: Agent-as-a-Verifier：基于证据而非分数的通用验证框架
authors:
- Yuxuan Sun
- Hao
- Chen
- Nagarajan Natarajan
- Sushrut Karmalkar
- Niranjani Prasad
- Amit Sharma
- Hongxiang Fan
affiliations:
- Imperial College London
- Microsoft Research
arxiv_id: '2611.34132'
url: https://arxiv.org/abs/2611.34132
pdf_url: https://arxiv.org/pdf/2611.34132
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 通用验证 · 可审计证据证书
tags:
- Agent
- Verification
- LLM
- Multi-Role
- Reward-Hacking
- Auditable-Evidence
one_liner: 提出多角色Agent结合形式化协议的通用验证框架，输出可审计证据证书，优于传统分数型验证器
practical_value: '- 多角色分离的验证架构可直接复用在电商推荐/广告的结果审核场景：将合规校验、事实校验、用户体验校验拆分给不同独立Agent角色，避免单模型判断偏差，同时留存全链路审核证据满足回溯需求

  - best-of-N选优场景可替换传统LLM-as-a-Judge的分数排序逻辑：改用`VERIFIED > SUPPORTED > PARTIAL`的等级排序规则，解决分数扎堆导致的排序不准问题，比如商品文案、广告创意的best-of-N选优，可直接提升选准率

  - 奖励黑客识别能力可复用在推荐系统黑产攻击检测、广告投放刷量作弊识别：通过自动生成反例的验证逻辑，识别能骗过基础规则的作弊行为，降低漏判率

  - 可审计证书生成机制可直接用于合规类审核场景：比如商品宣传语虚假宣传校验、直播内容合规审核，每一条裁决都附带完整证据链，满足监管要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于分数的LLM验证器/奖励模型仅输出标量分数，无明确可审计的证据支撑，易被话术引导、奖励黑客欺骗，且77%的分数集中在0.45-0.55区间，扎堆时排序准确性极低；现有生成式反馈验证器未充分利用Agent的工具调用、迭代推理能力，无法满足细粒度事实校验、复杂任务验证需求。
### 方法关键点
- 采用形式化协议驱动的多角色Agent架构，6个独立LLM角色（提取器、编译器、批评家、预言机、执行器、裁判）完全隔离，仅通过结构化对象交互，无共享会话状态，避免自证偏差
- 验证过程不输出分数，而是生成包含声明DAG、检查义务、证据链、最终裁决的可重放证书，裁决分为`VERIFIED/SUPPORTED/PARTIAL/UNVERIFIED/REFUTED`五个等级，按等级排序优先级远高于分数
- 支持离线best-of-N选优和在线Agent执行过程中的实时校验两种模式，可自动识别骗过基准评估器的奖励黑客行为
### 关键结果
- 离线best-of-5选优在Terminal-Bench 2.1数据集的36个混合结果任务子集上准确率达30/36，比同底座的LLM-as-a-Verifier（24/36）多正确选出6个任务的最优解，接近36/36的理论上限
- 在线嵌入Agent执行流程时，在FrontierMath（12题）、Terminal-Bench 2.1（87题）、CyberGym（50题）三个数据集上，分别比普通Agent提升3、10、8题的通过率
- 成功识别出骗过官方基准评估器的奖励黑客样本，生成可重放的反例证据
### 核心结论
验证的核心价值不是给出一个主观分数，而是输出可审计、可重放、可证伪的证据链，从根源上避免分数型验证的固有偏差和被攻击风险
