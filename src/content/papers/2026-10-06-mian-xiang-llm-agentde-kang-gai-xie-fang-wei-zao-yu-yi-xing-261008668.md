---
title: 'Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant
  Provenance for LLM Agents'
title_zh: 面向LLM Agent的抗改写防伪造语义行为水印技术
authors:
- Suxin Ji
- Hungtao Wan
- Shaoxuan Chen
- An Zhang
affiliations:
- University of Pennsylvania
- University of Massachusetts Amherst
- Chongqing University
- Independent Researcher
arxiv_id: '2610.08668'
url: https://arxiv.org/abs/2610.08668
pdf_url: https://arxiv.org/pdf/2610.08668
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 行为水印 抗改写防伪造
tags:
- Agent-Watermark
- Behavioral-Watermark
- Semantic-Cluster
- Anti-Forgery
- Paraphrase-Robust
one_liner: 提出训练无关的语义行为水印，解决现有Agent水印改写脆弱、易伪造的痛点
practical_value: '- 电商导购Agent、广告投放Agent的IP保护可直接复用该方案，无需训练，接入现有语义编码器即可上线，适配工具调用、文案生成等多类Agent场景

  - 语义簇作为水印载体的设计可迁移至推荐文案溯源、用户Query改写追踪等场景，无需绑定原始字符串，抗改写鲁棒性远高于字符串级方案

  - 密钥随机投影防伪造逻辑可复用在Agent轨迹合规审计场景，将投影维度r设为64即可将新鲜动作伪造率压至1%左右的FPR水平，满足监管要求

  - 历史窗口w的调优经验可直接复用：优先选w=1平衡删除鲁棒性和改写抗性，追求高检测率可升为w=3，适配不同业务的安全优先级'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent行为水印均绑定精确动作字符串，存在两大核心缺陷：一是语义改写/工具重命名后检测率骤降，AgentMark在改写场景下比特恢复率仅16.8%；二是完全无防伪造能力，攻击者可通过观察少量轨迹复现水印规则，伪造轨迹冒用身份，无法满足Agent商业化部署的IP保护和溯源需求。

### 方法关键点
- 完全训练无关：基于现成语义编码器对Agent动作做k-means聚类，以语义簇而非原始字符串作为水印载体，历史窗口也绑定簇ID，天然抗语义改写和工具重命名
- 密钥抗碰撞分桶：引入密钥控制的随机投影与哈希分桶机制，公开聚类结构不会泄露绿/红簇规则，随机谕言机模型下可证明未见过的动作分桶不可预测
- 低边际动作弃权：将簇归属置信度低的动作设为弃权位不携带水印，降低改写导致的比特错误率
- 采用随机密钥置换检验做检测，位置无关，天然抗步骤删除

### 关键结果
在ToolBench（600条轨迹/模型，覆盖5款3B-14B主流Agent）、ALFWorld（100条/模型）测试，对比Exact-symbol SeqWM、AgentMark等基线：
- 改写场景下TPR@1%FPR达0.49~0.66（ToolBench）、0.92~0.97（ALFWorld），基线仅为0.05~0.17、0.00~0.01
- 密钥投影维度r=64时，新鲜动作伪造率从100%降至1.2%，达到FPR基线水平
- 改写抗性的代价为单步水印容量损失约50%，无水印动作选择一致性保持72%~83%

> 最值得记住：Agent行为水印必须绑定语义而非原始字符串才能兼顾鲁棒性，防伪造必须引入密钥依赖的分桶逻辑，不能依赖公开聚类结构
