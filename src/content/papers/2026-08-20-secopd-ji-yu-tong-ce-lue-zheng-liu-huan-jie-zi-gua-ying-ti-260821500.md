---
title: 'SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation'
title_zh: SecOPD：基于同策略蒸馏缓解自适应提示注入攻击
authors:
- Yibo Peng
- Long Lian
- David Wagner
- Sizhe Chen
affiliations:
- University of California, Berkeley
arxiv_id: '2608.21500'
url: https://arxiv.org/abs/2608.21500
pdf_url: https://arxiv.org/pdf/2608.21500
published: '2026-08-20'
collected: '2026-08-27'
category: Agent
direction: Agent安全 · 提示注入防御
tags:
- Prompt Injection
- On-Policy Distillation
- LLM Security
- AI Agent
- Defensive Fine-tuning
one_liner: 通过基于干净输入的token级同策略蒸馏，将自适应提示注入攻击成功率降低一个数量级
practical_value: '- 电商导购/客服Agent接入商品详情、用户评论等非信任外部数据时，可参考SecOPD的信任域标记+干净输入蒸馏思路，无需额外标注安全数据集即可训练模型忽略非信任域内的恶意指令，避免诱导用户跳转、输出违规内容等问题

  - 生成式推荐、文案生成等场景用DPO/GRPO做合规对齐时，可借鉴token级反馈的设计，解决序列级奖励无法区分混合响应中合规/违规片段的问题，提升对齐精度同时降低效用损失

  - Agent工具调用安全优化可复用跨域泛化结论：仅在文本指令场景训练的提示注入防御能力可直接迁移到工具调用场景，无需额外标注工具域的攻击样本，大幅降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
提示注入是AI Agent的头号安全威胁，当Agent接入网页、文件、用户生成内容等非信任数据时，极易被注入的恶意指令劫持，现有基于DPO/GRPO的防御微调方案仅使用序列级反馈，无法区分混合响应中符合用户合法指令的部分和遵循恶意注入的部分，面对自适应攻击时SOTA防御方法的攻击成功率接近100%，严重阻碍Agent的规模化落地。

### 方法关键点
- 训练样本构造：对每条干净的<可信指令，非信任数据>对，生成对应的注入攻击样本，二者仅非信任数据域是否包含恶意注入有差异，其余完全一致
- 跨上下文token级打分：学生模型在注入样本上生成输出，用同初始化的frozen教师模型在对应干净输入上对每个输出token打分，教师打分高于学生的token给正反馈，反之给负反馈
- 训练流程：基于token级优势值更新学生模型，无需外部安全标注或奖励模型，所有监督信号均来自干净输入下的原始模型行为

### 关键实验
在SEP指令跟随基准、AgentDojo工具调用基准上测试，对比原始模型、SOTA防御方法Meta-SecAlign、GRPO序列级训练基线：基于Qwen3.6-27B微调的SecOPD模型面对SOTA自适应攻击PISmith的成功率仅9.0%，远低于Meta-SecAlign的94.0%；跨域到未见过的Agent工具调用场景，攻击成功率仅4.7%，优于Meta-SecAlign的5.5%；同时模型整体效用保留率达98%以上，仅比原始模型低1.3个百分点。

最值得记住的一句话：仅需明确划分输入的信任/非信任边界，基于token级同策略蒸馏即可在几乎不损失模型效用的前提下，大幅提升对自适应提示注入的防御能力
