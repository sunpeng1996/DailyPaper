---
title: 'AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks'
title_zh: AREX-2：基于长程反思任务的自进化智能体优化
authors:
- Hongjin Qian
- Chaofan Li
- Kun Luo
- Wenqing Wei
- Jianlyu Chen
- Shuqi Lu
- Yuyang Hu
- Hongwang Xiao
- Hui Wang
- Chaozhuo Li
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2609.38288'
url: https://arxiv.org/abs/2609.38288
pdf_url: https://arxiv.org/pdf/2609.38288
published: '2026-09-28'
collected: '2026-10-01'
category: Agent
direction: Agent自进化 · 长程反思训练
tags:
- Self-Improving-Agent
- Long-Horizon-Reasoning
- Reflection-Training
- Cross-Domain-Transfer
- Agent-Evaluation
one_liner: 基于MLE与编程领域长程迭代轨迹训练，实现跨域可迁移的高能力自进化智能体
practical_value: '- 做业务Agent迭代训练时，无需仅筛选单步成功样本，可保留完整迭代轨迹（含失败、回撤步骤），按最终效果筛选全轨迹做训练，能显著提升长任务下的容错与持续优化能力，适用于电商导购Agent、推荐策略调优Agent等场景

  - 长程反思是通用元技能，可先在反馈明确的领域（如广告素材A/B测试优化、推荐策略效果调优）做训练，再迁移到反馈模糊的场景（如用户满意度提升、深度内容搜索），大幅降低训练数据门槛

  - 业务Agent落地时可把通用操作知识（如平台规则、工具API说明）作为skill提前注入上下文，配合少量微调就能大幅提升基线效果，无需从头训练大模型，适配业务快速迭代需求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent的迭代优化逻辑大多由外层脚手架实现，模型本身不具备自主持续改进能力；训练数据多为单步成功样本，缺乏长程迭代、失败重试的轨迹学习，导致多轮任务下容易提前停滞，无法把更多计算资源转化为更好的输出效果，长程反思能力是实现真正自进化Agent的核心瓶颈。

### 方法关键点
- 明确长程反思是跨域通用元技能，选择反馈明确、迭代空间充足的MLE工程、算法编程两个领域构建训练环境，环境需满足参考方案可运行、基线效果远低于参考的条件，确保有足够迭代空间
- 构造训练轨迹时给Agent充足的迭代轮次与时间预算，保留完整轨迹（包括失败、效果回归、无效尝试），仅按最终效果与流程合规性筛选全轨迹，不淘汰单步失败的样本
- 训练时仅对推动效果提升的决策计算损失，无效操作、系统反馈、检索文档不参与损失计算，基于Qwen3.8-27B微调，同时保留原AREX的深度研究训练数据

### 关键实验
在6个基准测试上验证：① 训练域：MLE-bench Lite得分81.8，超过所有闭源/开源基线；Frontier-CS得分70.7，为开源模型最优水平，27B参数效果远超更大参数的基线模型；② 跨域迁移（无新增研究类训练数据）：BrowseComp 84.0、HLE 52.6、GAIA 92.2、DeepSearchQA 93.8，效果超过上一代122B参数的AREX模型；③ 多轮缩放：Frontier-CS任务下5小时内持续提升，最后1小时仍有2.2分增益，远超基线2-3小时就停滞的表现。

### 核心结论
长程反思能力是可迁移的元技能，在易监督的领域训练的迭代优化能力，可以直接迁移到缺乏明确反馈的复杂任务场景。
