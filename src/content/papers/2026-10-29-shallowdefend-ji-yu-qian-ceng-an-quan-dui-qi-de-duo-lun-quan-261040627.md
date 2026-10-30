---
title: 'ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender'
title_zh: ShallowDefend：基于浅层安全对齐的多轮LLM安全防御框架
authors:
- Qiyao Ma
- Xiaodong Liu
- Weiwei Yang
- Mingqian Feng
- Chengquan Guo
- Jialin Song
- Carolyn Buractaon
- Zhe Zhao
- Junshan Zhang
- Sandeep Atluri
affiliations:
- University of California, Davis
- Microsoft Research
arxiv_id: '2610.40627'
url: https://arxiv.org/abs/2610.40627
pdf_url: https://arxiv.org/pdf/2610.40627
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: LLM安全 · 多轮对话防御
tags:
- LLM Safety
- Multi-turn Dialogue
- Safety Alignment
- Reinforcement Learning
- GRPO
one_liner: 将LLM安全对齐的浅层特性从漏洞转为可控决策点，实现高效多轮对话安全防御
practical_value: '- 电商导购/客服Agent、多轮对话推荐系统可直接复用Assess→Decide→Respond框架，在生成用户回复前增加显式安全决策步骤，可低成本抵御多轮越狱攻击，避免诱导输出违规承诺、内部信息等内容

  - 安全对齐训练可复用规则自校验奖励设计，仅需知道训练对话的有害/良性标签即可完成训练，无需额外标注安全回复、无需外接Judge模型，大幅降低中小业务的安全对齐成本

  - 工程上可将决策模块做成可插拔前置组件，仅需修改系统prompt，对原有LLM的推理逻辑、回复生成风格影响极小，同时保留99%以上的基座模型效用

  - 搜索推荐场景的多轮query理解可复用显式决策+规则校验思路，提前识别用户拆分到多轮的违规商品检索需求，无需改动原有召回排序逻辑即可实现前置拦截'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM单轮安全对齐已能稳定拒绝直接有害请求，但多轮对话场景下攻击者可将恶意需求拆分到多轮，每轮语义无害即可绕过防御。其核心机制漏洞是安全对齐的「浅层性」：安全行为仅集中在输出前几个token，一旦回复开头偏向合规应答，后续生成就会回归基座模型逻辑。现有防御高度依赖标注数据或外部Judge模型，成本高、泛化性差，且没有显式的安全决策控制点。

### 方法关键点
- 采用**Assess→Decide→Respond**三段式生成流程：每轮先评估用户隐藏意图与潜在危害，输出可被规则解析的显式安全决策（COMPLY/REFUSE/SAFE-REDIRECT），再基于决策生成用户可见回复，决策与回复绑定，修改决策即可控制回复走向
- 设计两种低成本奖励：规则自校验奖励仅比对最终轮决策与对话预定义的有害/良性标签，无需标注、无需外部模型；LLM-as-Judge奖励支持分级决策与安全重定向，适配更复杂场景
- 训练用GRPO优化，仅在多轮攻击的最终payload轮回传梯度，避免前期无害轮次稀释训练信号，同时设置单轮token上限防止奖励hack

### 关键结果
在Llama3.1-8B-Instruct、Qwen3-8B两个基座上与SFT、DPO、MTSA等7个基线对比，覆盖14个安全、效用、友好性基准：自校验奖励版本平均安全率在Llama上达90.4%，比最优基线高4.1pp，Qwen上达93.4%，比最优基线高7.7pp；基座效用保留率超99%，仅过度拒绝率有可接受的小幅上升。

### 核心结论
不要把LLM对齐的固有特性都视为缺陷，转换思路即可将攻击者瞄准的漏洞转化为最高效的干预控制点
