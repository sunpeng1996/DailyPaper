---
title: 'The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks'
title_zh: 编码Agent工作集机制：仓库级任务的一致性债务研究
authors:
- Bardia Mohammadi
- Lars Klein
- Aman Chadha
- Akhil Arora
- Laurent Bindschaedler
affiliations:
- Max Planck Institute for Software Systems
- EPFL
- Apple
- Aarhus University
arxiv_id: '2608.16630'
url: https://arxiv.org/abs/2608.16630
pdf_url: https://arxiv.org/pdf/2608.16630
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 编码Agent · 仓库级任务一致性优化
tags:
- Coding Agent
- Coherence Debt
- Repository Task
- Working Set
- LLM Agent
one_liner: 通过受控实验揭示编码Agent双渠道事实获取规律，给出一致性债务量化方法与工具链优化方向
practical_value: '- 做电商场景下营销规则生成、商品合规校验等强一致性要求的Agent时，必须将编辑依赖的所有规则（如满减阈值、违禁词规则）显式放入上下文或通过专项微调注入参数记忆，避免因一致性债务生成错误配置

  - 优化Agent工具链成本时，不要盲目增大上下文或拆分多Agent，先梳理任务耦合依赖图，强耦合任务不要跨Agent拆分；实验显示相同通过率的配置token消耗差异可达12.8倍，冗余请求完全无收益

  - 设计Agent交互流程时，可要求Agent编辑前显式声明依赖的事实与版本，避免缺事实时Agent直接编造结果；优先选择会主动上报缺失依赖的模型，降低错误排查成本

  - 维护Agent参考知识库时，必须及时清理过期规则，过时的书面规范会被Agent优先遵循，哪怕和实际正确配置冲突，错误引导的危害远大于无规范'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前仓库级编码Agent执行跨文件迁移、Bug修复等任务时，跨文件一致性错误占比极高，但现有评测仅关注最终输出，无法定位编辑时刻依赖事实缺失的根因；参数记忆和上下文的可替代性、任务耦合对结果的影响也缺乏明确的量化结论，制约了编码Agent的效果和效率优化。

### 方法关键点
1. 提出一致性债务量化模型：编辑需满足的耦合事实若未出现在有效上下文、也不在模型参数记忆中，即产生一致性债务，债务规模直接关联编辑错误率；
2. 设计三组受控实验：虚构API迁移（消弭模型先验）、真实Pydantic迁移+改名对照（控制参数记忆有效性）、合成耦合任务（已知所有依赖事实），分别隔离上下文、参数记忆、任务耦合三个变量的影响；
3. 提出5类事件日志规范，可用于回放Agent执行过程，定位一致性债务的产生环节。

### 关键结果
1. 零上下文+零任务先验的154次虚构API迁移实验全部失败，将所需事实全部放入prompt后300次实验中299次达到9/12以上正确率，213次全对；
2. 7个模型在改名后的Pydantic迁移任务上66/70次都卡在相同的24/79分，错误的测试用例完全一致，验证了参数记忆的边界；
3. 全部通过测试的不同工具链配置，token消耗差异可达12.8倍，冗余请求无任何额外收益，缺事实时多消耗token也无法提升成功率；
4. 书面规范和实际代码冲突时，39次实验中Agent100%遵循书面规范，哪怕规范要求的是更差的实现，过时规范的危害远大于无规范。

### 最值得记住的结论
编码Agent的成功率仅由编辑时刻依赖的事实是否存在（无论来自上下文还是参数记忆）决定，和上下文长度、事实在上下文中的位置无关。
