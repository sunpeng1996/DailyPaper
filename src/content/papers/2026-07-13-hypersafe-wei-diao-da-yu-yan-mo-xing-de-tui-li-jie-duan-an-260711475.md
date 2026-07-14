---
title: 'HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models'
title_zh: HyperSafe：微调大语言模型的推理阶段安全恢复框架
authors:
- Aznaur Aliev
- Carlos Hinojosa
- Abdelrahman Eldesokey
- Bang An
- Bernard Ghanem
- Yibo Yang
affiliations:
- King Abdullah University of Science and Technology
arxiv_id: '2607.11475'
url: https://arxiv.org/abs/2607.11475
pdf_url: https://arxiv.org/pdf/2607.11475
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: LLM安全对齐 · 推理阶段防护
tags:
- LLM Safety
- Fine-tuning
- Hypernetwork
- Side Network
- Inference Defense
one_liner: 通过超网络生成模型专属轻量安全侧网络，无需修改权重即可恢复微调LLM的安全对齐能力
practical_value: '- 业务中使用微调LLM做推荐文案生成、智能客服回复、Agent决策时，可直接复用HyperSafe的侧网络+选择性路由架构，无需修改原模型权重即可叠加安全防护，避免违规内容输出，同时几乎不损失任务性能

  - 可借鉴「激活指纹+超网络生成专属小模型」的思路，针对业务不同场景的微调checkpoint，无需逐个训练安全分类器，一次超网络前向即可生成对应安全侧网络，大幅降低多checkpoint场景的部署成本

  - 侧网络的阶梯连接隐态融合设计可迁移到其他模型诊断、异常输入检测场景，通过捕获主干模型的层激活变化实现定制化检测，比通用分类器准确率更高、开销更低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
对齐后的LLM即使基于完全良性数据微调，安全对齐能力也会出现明显退化，有害响应率可从基线的5%以下升至40%以上；现有防护方案存在三类缺陷：微调阶段加约束会引入安全-效用tradeoff、事后修改模型权重易导致任务能力遗忘、通用安全分类器无法捕获特定微调模型的特有安全风险，亟需无侵入、模型专属、低开销的事后安全恢复方案。

### 方法关键点
1. 提取微调模型的层激活指纹：用少量校准prompt的每层最后token隐态平均值表征模型的微调偏移特征，对激活做方向-幅值分解后聚合为全局表示
2. 预训练超网络以激活指纹为输入，仅需一次前向即可生成轻量Safe Side Network（SSN）权重，SSN仅占7-8B级主模型参数的3-4%，通过阶梯连接融合主干隐态实现prompt级安全分类
3. 推理阶段采用选择性路由：判定为安全的请求完全走原微调模型输出，有害请求直接返回拒答，全程不修改原模型权重，部署阶段无需安全标注数据与梯度更新

### 关键结果
在Qwen2-7B、LLaMA-3-8B两个模型族共22个下游微调场景测试：
- 微调后模型的有害响应率从19%~31%降至1%以下，零样本安全基准AdvBench、HEx-PHI上有害率均为0%，显著优于Llama Guard 4的6.5%、6.7%漏检率
- 下游任务准确率平均仅比无防护的微调基线低1%以内
- 仅需50条校准prompt即可达到最优效果，单模型SSN生成耗时小于1分钟

最值得记住的结论：同一款基础模型的所有微调checkpoint，仅需一个预训练好的HyperSafe超网络，无需额外对齐即可快速恢复安全能力，完全不影响原模型的任务表现。
