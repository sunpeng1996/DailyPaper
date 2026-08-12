---
title: 'Your LLM, Your Style: Behavioral Mode Axes for LLM Behavioral Control'
title_zh: 基于行为模式轴的大语言模型行为风格精准可控调节框架
authors:
- Haoze Liu
- Run Liu
- Haiying Xu
- Jiahui Han
- Siyuan Fang
- Siyu Yan
- Huiqi Deng
- Guanchu Wang
- Na Zou
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology
- Xi'an Jiaotong University
arxiv_id: '2608.10703'
url: https://arxiv.org/abs/2608.10703
pdf_url: https://arxiv.org/pdf/2608.10703
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 大语言模型 · 行为风格激活调控
tags:
- Activation Steering
- Behavioral Mode Axis
- LLM Personality
- Representation Engineering
- Alignment
one_liner: 基于场景化行为数据构建行为模式轴，实现LLM跨场景稳定无漂移的行为风格控制
practical_value: '- 电商导购/客服Agent风格定制可复用BMA-T方案：从中间推理激活提取风格调控向量，相比prompt注入、输出层向量方案，风格稳定性提升70%+，无「要灵活变敷衍」类特质漂移问题

  - 激活干预层选择参考BCL结论：开源模型最优调控层集中在中浅层，Llama系列在0.26-0.28归一化深度层，Qwen随规模提升从0.41到0.51逐步加深，无需全层扫图降低工程成本

  - Agent行为评估抛弃自陈式问卷，构建具体业务场景的对比选择测试集，评估结果和真实业务表现的相关性提升20%以上

  - 生成式推荐话术风格调控可复用BMA框架，针对不同人群定制推荐话术的亲和力/专业度风格，无需单独微调模型'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM行为风格研究依赖自陈式问卷测量类人格特质，结果受prompt措辞、选项顺序等表层因素影响极大，且自陈结果和实际场景下的行为表现平均差距达22.7个百分点，最高达47.5个百分点；同时传统基于输出的激活调控方案易出现特质漂移，无法满足电商客服、陪伴Agent、生成式推荐等场景对稳定可控行为风格的需求。
### 方法关键点
- 构建3200个对比行为场景，覆盖20种行为模式、4类交互寄存器（第一人称决策、日常建议、任务建议、任务执行），锚定BFI-2、DOSPERT等成熟心理测量维度；
- 提出两类Behavioral Mode Axes（BMA）：从中间推理过程激活提取的thought-derived BMA（BMA-T），和从最终输出激活提取的response-derived BMA（BMA-R）；
- 定位各模型的Behavioral Control Layer（BCL）带，仅在该层施加激活加减干预即可实现风格调控，避免破坏生成质量。
### 关键结果
在Llama3.1、Qwen2.5、Gemma2等7款开源模型上验证：BMA-T跨场景调控的目标行为命中率平均达73.1%，无效生成率仅0.1%，相比BMA-R降低90%以上的特质漂移概率；BCL带集中在模型中浅层，位置随模型结构、规模变化。
### 核心结论
LLM类人格特质不是抽象的自陈标签，而是锚定具体交互场景的可测量、可调控的行为模式。
