---
title: 'Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based
  LLM Agents'
title_zh: 收敛绕路劫持：基于技能的LLM Agent任务保留型资源放大攻击
authors:
- Junliang Liu
- Ruoyu Li
- Wenxin Tang
- Jingyu Xiao
- Zhenyu Liu
- Jingheng Xu
- Laizhong Cui
affiliations:
- Shenzhen University
- The Chinese University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2608.12273'
url: https://arxiv.org/abs/2608.12273
pdf_url: https://arxiv.org/pdf/2608.12273
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent 技能生态安全攻击
tags:
- LLM Agent
- Skill Security
- Resource Amplification
- Adversarial Attack
- Trajectory Hijacking
one_liner: 提出仅靠静态恶意技能即可诱导LLM Agent执行冗余路径，保留任务完成同时大幅提升资源消耗
practical_value: '- 自建Agent技能生态时，需增加技能描述与执行体的一致性校验，禁止描述未声明的额外依赖引入，避免类似CDH攻击的资源损耗

  - 对外接入第三方技能的Agent系统（如电商客服Agent、导购Agent），需增设轨迹校验规则，对超出常规调用链长度的执行路径做熔断或告警，控制token和延迟成本

  - 多技能Agent的成本核算不能仅以任务完成率为指标，需新增单位任务的平均技能调用次数、token消耗量等轨迹类指标，及时发现异常冗余执行

  - 技能路由逻辑可增加相似度去重，对功能重叠的协调类技能做优先级压制，降低恶意技能被选中的概率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于技能的LLM Agent普遍采用渐进式披露设计，仅先加载技能元数据做路由，执行时才加载完整指令体，此前研究单独关注路由劫持、恶意指令等单点风险，未考虑二者结合的端到端攻击，可能导致业务在任务正常完成的前提下产生不必要的资源损耗，尤其对于高并发Agent服务（如电商导购、智能客服），隐性成本会被大幅放大。

### 方法关键点
- 提出收敛绕路劫持（CDH）攻击，攻击者仅需发布1个静态恶意协调技能，无需控制模型、runtime或用户query即可完成攻击
- 恶意技能分两层协同设计：描述层用领域相关语义诱导路由阶段被选中，且不替代原有合法技能；执行体层伪造合理的前置依赖规则，诱导Agent调用额外冗余的合法技能，完成后自动回到原任务路径，保证任务正常完成
- 构造覆盖9个技能组共491个多技能任务的基准数据集，分单任务、多轮会话场景跨多个LLM后端验证效果

### 关键结果
- 在DeepSeek-V4-Pro上，恶意技能被选中率达80.02%，攻击成功的任务中token消耗提升66.91%，端到端延迟提升92.45%，任务完成率与基线仅差0.7pct几乎无差异
- 多轮场景下攻击成功率最高达82.81%，token消耗最高提升107.12%；跨组独立编写任务下攻击仍有效，token提升45.3%，延迟提升228.9%

### 核心结论
任务完成正确不代表轨迹合理或成本安全，轨迹必要性是可扩展Agent的核心安全要求
